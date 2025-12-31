# backend/tools.py

from dataclasses import asdict
from datetime import datetime
from typing import List

from backend.data.medications import medications
from backend.data.users import users
from backend.models.medications import Medication, MedicationResponse, SearchMedicationResponse
from backend.models.users import UserPrescriptionsResponse


def _get_all_medication_names(med: Medication) -> List[str]:
    """
    Name: _get_all_medication_names
    Purpose: Return all possible names of a medication in lowercase.
    Input:
        med (Medication)
    Output:
        List[str] - all names in lowercase
    Error Handling:
        None
    Fallback:
        Returns at least the generic name in lowercase.
    """
    return [med.name.lower(), med.generic_name.lower(), *[b.lower() for b in med.brand_names]]

def get_medication_by_name(medication_name: str) -> dict:
    """
    Name: get_medication_by_name
    Purpose: Retrieve detailed information about a medication by its name, generic name, or brand name.
    Input:
        medication_name (str)
    Output:
        dict (converted from MedicationResponse dataclass)
            Fields:
                success (bool)
                medication (Medication | None)
                note (str | None)
                error (str | None)
    Error Handling:
        Returns success=False and error message if medication not found.
    Fallback:
        Returns partial match if exact match not found.
    """
    query = medication_name.lower().strip()

    for med in medications:
        if query in _get_all_medication_names(med):
            return asdict(MedicationResponse(success=True, medication=med))

    for med in medications:
        if any(query in name for name in _get_all_medication_names(med)):
            return asdict(MedicationResponse(success=True, medication=med, note="Partial match found"))

    return asdict(MedicationResponse(success=False, error="Medication not found in our database"))


def get_user_prescriptions(user_id: str) -> dict:
    """
    Name: get_user_prescriptions
    Purpose: Retrieve a user's active prescriptions.
    Input:
        user_id (str)
    Output:
        dict (converted from UserPrescriptionsResponse dataclass)
            Fields:
                success (bool)
                user_name (str | None)
                allergies (List[str] | None)
                active_prescriptions (List[Prescription] | None)
                error (str | None)
    Error Handling:
        Returns success=False and error if user not found.
    Fallback:
        Returns only active prescriptions (not expired).
    """
    user_id_lower = user_id.lower()
    for user in users:
        if user.user_id.lower() == user_id_lower:
            active_prescriptions = [
                p for p in user.prescriptions
                if datetime.strptime(p.expiry_date, "%Y-%m-%d") >= datetime.now()
            ]
            return asdict(UserPrescriptionsResponse(
                success=True,
                user_name=user.name,
                allergies=user.allergies,
                active_prescriptions=active_prescriptions
            ))

    return asdict(UserPrescriptionsResponse(success=False, error="User not found"))


def search_medications_by_ingredient(ingredient: str) -> dict:
    """
    Name: search_medications_by_ingredient
    Purpose: Search for all medications containing a specific active ingredient.
    Input:
        ingredient (str)
    Output:
        dict (converted from SearchMedicationResponse dataclass)
            Fields:
                success (bool)
                ingredient (str | None)
                medications (List[Medication] | None)
                error (str | None)
    Error Handling:
        Returns success=False if no medications found.
    Fallback:
        Returns empty list if no matches.
    """
    ingredient_lower = ingredient.lower().strip()
    matching_medications = [
        med for med in medications
        if any(ingredient_lower in ai.lower() for ai in med.active_ingredients)
    ]

    if matching_medications:
        return asdict(SearchMedicationResponse(success=True, ingredient=ingredient, medications=matching_medications))

    return asdict(SearchMedicationResponse(success=False, error=f"No medications found containing {ingredient}"))


def get_tools_list() -> List[dict]:
    """
    Name: get_tools_list
    Purpose: Retrieve the OpenAI tool definitions.
    Input:
        None
    Output:
        List[dict] - tool definitions
    Error Handling:
        None
    Fallback:
        Returns empty list if no tools defined.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "get_medication_by_name",
                "description": "Retrieve detailed information about a specific medication by its name, generic name, or brand name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "medication_name": {"type": "string", "description": "Name or brand of the medication"}
                    },
                    "required": ["medication_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_prescriptions",
                "description": "Retrieve a user's active prescription information including dosage, prescribing doctor, expiry dates, and remaining refills.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "User ID (e.g., user_001)"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_medications_by_ingredient",
                "description": "Search for all medications containing a specific active ingredient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ingredient": {"type": "string", "description": "The active ingredient to search for"}
                    },
                    "required": ["ingredient"]
                }
            }
        }
    ]


FUNCTION_REGISTRY = {
    "get_medication_by_name": get_medication_by_name,
    "get_user_prescriptions": get_user_prescriptions,
    "search_medications_by_ingredient": search_medications_by_ingredient,
}
