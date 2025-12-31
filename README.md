# Pharmacy AI Assistant

## Overview
This project is a **Pharmacy AI Assistant** designed to assist users in retrieving information about medications, checking prescription details, and searching medications by active ingredients. The assistant is powered by **OpenAI API** and a local db.

The system provides a web frontend served by a Flask backend. The backend handles streaming chat interactions, executes specific tool functions, and ensures that only factual information from the pharmacy db is returned.

## Architecture

```
├── backend/
│   ├── data/                # Mock data for medications and users
│   ├── models/              # Dataclasses for Medications, Users, and responses
│   ├── agent.py             # OpenAI integration and chat streaming
│   ├── config.py            # Environment variables and system prompt
│   ├── main.py              # Flask with endpoint
│   └── tools.py             # Tool functions callable by the agent
    └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # Simple UI for interacting with the assistant
├── .env                     # API keys and configuration
├── Dockerfile               # Docker configuration

```

**Backend Details:**
- `main.py` exposes:
  - `/chat` endpoint: handles chat messages with streaming responses.
  - `/health` endpoint: returns service health status.
  - `/` endpoint: serves the frontend `index.html` 
- `tools.py` provides functions the AI can call:
  - `get_medication_by_name`
  - `get_user_prescriptions`
  - `search_medications_by_ingredient`
- `agent.py` connects to OpenAI and streams responses, handling tool calls dynamically.

**Frontend Details:**
- `index.html` provides a simple chat interface that communicates with `/chat` endpoint.

**Running with Docker:**

1. Build the Docker image:

```bash
docker build -t pharmacy-agent .
```

2. Run the container:

```bash
docker run -p 5000:5000 pharmacy-agent
```

3. Open your browser and navigate to:

```
http://localhost:5000/
```

**Notes:**
- `.env` is copied into the Docker image and contains `OPENAI_API_KEY` and `OPENAI_MODEL`.
- No external environment variables are required when running the container.

## Multi-Step Flow Examples

1. **Retrieve medication by name**
   - User: "יש לכם אדוויל?"
   - Agent: מחזיר - "כן, יש לנו אדוויל במלאי, 780 יחידות".
  
<img width="700" height="519" alt="צילום מסך 2025-12-31 141941" src="https://github.com/user-attachments/assets/af351195-a77c-425a-97c8-e4298c9638d6" />
<img width="600" height="505" alt="צילום מסך 2025-12-31 135910" src="https://github.com/user-attachments/assets/25fb338f-f544-4ad0-a7d2-e6e391d7cbc8" />

2. **Check user prescriptions**
   - User: "Show my prescriptions for user_001"
   - Agent: Lists all active prescriptions, expiry dates, and dosage instructions.
     for example:
      "Here are the active prescriptions for David Cohen (user_001): 
      - Medication: Amoxicillin - Dosage: 500mg capsules - Quantity: 30 - Instructions: Take one capsule every 8 hours - Prescribing doctor: Dr. Sarah Levi - Issue date:             2025-12-15 - Expiry date: 2026-03-15 - Refills remaining: 2 Allergies on file: None known If you need anything else related to this prescription, let me know."
    
<img width="700" height="473" alt="צילום מסך 2025-12-31 135846" src="https://github.com/user-attachments/assets/b25a0485-168d-43c2-a455-9a50a1f7cb8d" />
<img width="700" height="454" alt="צילום מסך 2025-12-31 142202" src="https://github.com/user-attachments/assets/60123a07-5b56-4fb9-9d7c-1b8450696be4" />

3. **Search medications by ingredient**
   - User: "Which medications contain ibuprofen?"
   - Agent: Returns a list of medications with ibuprofen as an active ingredient.

<img width="680" height="518" alt="צילום מסך 2025-12-31 142157" src="https://github.com/user-attachments/assets/d3234ad2-148a-4553-81d5-82bb53571772" />
<img width="700" height="475" alt="צילום מסך 2025-12-31 142102" src="https://github.com/user-attachments/assets/155ac046-8892-4878-a00a-33462cf7db40" />


## Evaluation Plan

To evaluate the assistant:
1. **Accuracy**: Verify that the assistant only returns factual information from the database.
2. **Function execution**: Ensure that tool functions (`get_medication_by_name`, etc.) return correct results.
3. **Streaming behavior**: Confirm that multi-step interactions are streamed correctly.
4. **Error handling**: Test invalid inputs to confirm proper error responses.
5. **Safety checks**: Validate that the assistant never provides medical advice or recommendations.

**Author:** Meitav Ziv  
**Date:** 2025-12-31




