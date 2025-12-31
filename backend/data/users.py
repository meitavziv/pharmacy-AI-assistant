from backend.models.users import User, Prescription

users = [
    User(
        user_id="user_001",
        name="David Cohen",
        phone="052-1234567",
        email="david.cohen@email.com",
        date_of_birth="1985-03-15",
        prescriptions=[
            Prescription(
                medication_id="med_001",
                medication_name="Amoxicillin",
                prescribing_doctor="Dr. Sarah Levi",
                issue_date="2025-12-15",
                expiry_date="2026-03-15",
                refills_remaining=2,
                dosage="500mg capsules",
                quantity=30,
                instructions="Take one capsule every 8 hours"
            )
        ],
        allergies=["None known"]
    ),
    User(
        user_id="user_002",
        name="Rachel Mizrahi",
        phone="053-9876543",
        email="rachel.m@email.com",
        date_of_birth="1978-07-22",
        prescriptions=[
            Prescription(
                medication_id="med_003",
                medication_name="Metformin",
                prescribing_doctor="Dr. Michael Goldstein",
                issue_date="2025-11-01",
                expiry_date="2026-11-01",
                refills_remaining=5,
                dosage="500mg tablets",
                quantity=60,
                instructions="Take one tablet twice daily with meals"
            ),
            Prescription(
                medication_id="med_005",
                medication_name="Lisinopril",
                prescribing_doctor="Dr. Michael Goldstein",
                issue_date="2025-11-01",
                expiry_date="2026-11-01",
                refills_remaining=5,
                dosage="10mg tablets",
                quantity=30,
                instructions="Take one tablet once daily in the morning"
            )
        ],
        allergies=["Penicillin"]
    ),
    User(
        user_id="user_003",
        name="John Smith",
        phone="054-5551234",
        email="john.smith@email.com",
        date_of_birth="1990-11-30",
        prescriptions=[],
        allergies=["None known"]
    ),
    User(
        user_id="user_004",
        name="Maya Shapiro",
        phone="052-7778888",
        email="maya.shapiro@email.com",
        date_of_birth="1995-04-18",
        prescriptions=[
            Prescription(
                medication_id="med_001",
                medication_name="Amoxicillin",
                prescribing_doctor="Dr. Yael Ben-David",
                issue_date="2025-12-20",
                expiry_date="2026-01-20",
                refills_remaining=0,
                dosage="250mg capsules",
                quantity=21,
                instructions="Take one capsule every 8 hours for 7 days"
            )
        ],
        allergies=["Sulfa drugs"]
    ),
    User(
        user_id="user_005",
        name="Daniel Avraham",
        phone="053-4445555",
        email="daniel.a@email.com",
        date_of_birth="1982-09-05",
        prescriptions=[
            Prescription(
                medication_id="med_005",
                medication_name="Lisinopril",
                prescribing_doctor="Dr. Ruth Katz",
                issue_date="2025-10-15",
                expiry_date="2026-10-15",
                refills_remaining=6,
                dosage="20mg tablets",
                quantity=30,
                instructions="Take one tablet once daily"
            )
        ],
        allergies=["None known"]
    ),
    User(
        user_id="user_006",
        name="Sarah Johnson",
        phone="054-3332222",
        email="sarah.j@email.com",
        date_of_birth="1988-12-12",
        prescriptions=[],
        allergies=["Aspirin", "Penicillin"]
    ),
    User(
        user_id="user_007",
        name="Yossi Friedman",
        phone="052-9998877",
        email="yossi.f@email.com",
        date_of_birth="1975-06-25",
        prescriptions=[
            Prescription(
                medication_id="med_003",
                medication_name="Metformin",
                prescribing_doctor="Dr. David Rosenberg",
                issue_date="2025-09-01",
                expiry_date="2026-09-01",
                refills_remaining=8,
                dosage="850mg tablets",
                quantity=60,
                instructions="Take one tablet once daily with dinner"
            )
        ],
        allergies=["None known"]
    ),
    User(
        user_id="user_008",
        name="Emma Wilson",
        phone="053-6667777",
        email="emma.wilson@email.com",
        date_of_birth="1992-02-28",
        prescriptions=[],
        allergies=["None known"]
    ),
    User(
        user_id="user_009",
        name="Avi Klein",
        phone="054-1112233",
        email="avi.klein@email.com",
        date_of_birth="1980-08-08",
        prescriptions=[
            Prescription(
                medication_id="med_001",
                medication_name="Amoxicillin",
                prescribing_doctor="Dr. Tamar Cohen",
                issue_date="2025-12-28",
                expiry_date="2026-01-28",
                refills_remaining=1,
                dosage="500mg capsules",
                quantity=30,
                instructions="Take one capsule every 12 hours"
            )
        ],
        allergies=["Latex"]
    ),
    User(
        user_id="user_010",
        name="Leah Kaplan",
        phone="052-5554444",
        email="leah.kaplan@email.com",
        date_of_birth="1970-05-17",
        prescriptions=[
            Prescription(
                medication_id="med_005",
                medication_name="Lisinopril",
                prescribing_doctor="Dr. Moshe Stein",
                issue_date="2025-12-01",
                expiry_date="2026-12-01",
                refills_remaining=11,
                dosage="10mg tablets",
                quantity=30,
                instructions="Take one tablet once daily in the morning"
            ),
            Prescription(
                medication_id="med_004",
                medication_name="Omeprazole",
                prescribing_doctor="Dr. Moshe Stein",
                issue_date="2025-12-01",
                expiry_date="2026-06-01",
                refills_remaining=3,
                dosage="20mg capsules",
                quantity=30,
                instructions="Take one capsule once daily 30 minutes before breakfast"
            )
        ],
        allergies=["None known"]
    )
]
