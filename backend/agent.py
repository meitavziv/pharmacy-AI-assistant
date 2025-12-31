import json

from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL, SYSTEM_PROMPT
from tools import (
    get_tools_list, FUNCTION_REGISTRY
)

client = OpenAI(api_key=OPENAI_API_KEY)
tools = get_tools_list()

def execute_function(function_name, arguments):
    """Generic function executor"""

    func = FUNCTION_REGISTRY.get(function_name)

    if not func:
        return {"success": False, "error": f"Unknown function: {function_name}"}

    try:
        return func(**arguments)
    except TypeError as e:
        return {
            "success": False,
            "error": "Invalid arguments for function",
            "details": str(e)
        }


def chat_stream(messages):
    """Generates streaming responses for chat"""
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    def generate():
        try:
            stream = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=full_messages,
                tools=tools,
                stream=True
            )

            collected_messages = []
            function_calls = []

            for chunk in stream:
                delta = chunk.choices[0].delta

                if delta.content:
                    collected_messages.append(delta.content)
                    yield f"data: {json.dumps({'type': 'content', 'content': delta.content})}\n\n"

                if delta.tool_calls:
                    for tool_call in delta.tool_calls:
                        if tool_call.index is not None:
                            while len(function_calls) <= tool_call.index:
                                function_calls.append({"id": None, "name": None, "arguments": ""})

                            if tool_call.id:
                                function_calls[tool_call.index]["id"] = tool_call.id
                            if tool_call.function and tool_call.function.name:
                                function_calls[tool_call.index]["name"] = tool_call.function.name
                            if tool_call.function and tool_call.function.arguments:
                                function_calls[tool_call.index]["arguments"] += tool_call.function.arguments

                if chunk.choices[0].finish_reason == "tool_calls":
                    tool_call_messages = []
                    tool_result_messages = []

                    for func_call in function_calls:
                        if func_call["name"]:
                            yield f"data: {json.dumps({'type': 'tool_call', 'name': func_call['name'], 'arguments': func_call['arguments']})}\n\n"

                            arguments = json.loads(func_call["arguments"])
                            result = execute_function(func_call["name"], arguments)

                            yield f"data: {json.dumps({'type': 'tool_result', 'name': func_call['name'], 'result': result})}\n\n"

                            if not tool_call_messages:
                                tool_call_messages.append({
                                    "role": "assistant",
                                    "content": None,
                                    "tool_calls": []
                                })

                            tool_call_messages[0]["tool_calls"].append({
                                "id": func_call["id"],
                                "type": "function",
                                "function": {
                                    "name": func_call["name"],
                                    "arguments": func_call["arguments"]
                                }
                            })

                            tool_result_messages.append({
                                "role": "tool",
                                "content": json.dumps(result),
                                "tool_call_id": func_call["id"]
                            })

                    continuation_messages = full_messages + tool_call_messages + tool_result_messages

                    stream2 = client.chat.completions.create(
                        model=OPENAI_MODEL,
                        messages=continuation_messages,
                        stream=True
                    )

                    for chunk2 in stream2:
                        delta2 = chunk2.choices[0].delta
                        if delta2.content:
                            yield f"data: {json.dumps({'type': 'content', 'content': delta2.content})}\n\n"

                        if chunk2.choices[0].finish_reason == "stop":
                            yield f"data: {json.dumps({'type': 'done'})}\n\n"
                    break

                if chunk.choices[0].finish_reason == "stop":
                    yield f"data: {json.dumps({'type': 'done'})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"

    return generate
