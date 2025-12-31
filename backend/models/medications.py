# backend/models/medication.py

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Medication:
    id: str
    name: str
    generic_name: str
    brand_names: List[str]
    active_ingredients: List[str]
    dosage_form: str
    indication: str
    dosage_instructions: str
    side_effects: List[str]
    warnings: List[str]
    prescription_required: bool
    quantity_in_stock: int
    storage: str
    category: str

@dataclass
class MedicationResponse:
    success: bool
    medication: Optional[Medication] = None
    note: Optional[str] = None
    error: Optional[str] = None

@dataclass
class SearchMedicationResponse:
    success: bool
    ingredient: Optional[str] = None
    medications: Optional[List[Medication]] = None
    error: Optional[str] = None
