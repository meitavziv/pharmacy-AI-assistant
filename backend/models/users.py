# backend/models/user.py

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Prescription:
    medication_id: str
    medication_name: str
    prescribing_doctor: str
    issue_date: str
    expiry_date: str
    refills_remaining: int
    dosage: str
    quantity: int
    instructions: str

@dataclass
class User:
    user_id: str
    name: str
    phone: str
    email: str
    date_of_birth: str
    prescriptions: List[Prescription]
    allergies: List[str]

@dataclass
class UserPrescriptionsResponse:
    success: bool
    user_name: Optional[str] = None
    allergies: Optional[List[str]] = None
    active_prescriptions: Optional[List[Prescription]] = None
    error: Optional[str] = None
