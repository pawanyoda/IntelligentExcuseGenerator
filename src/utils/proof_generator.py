from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

class ProofGenerator:
    @staticmethod
    def generate_doctors_note():
        """Generate fake doctors note."""
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "doctor": f"Dr. {fake.last_name()}",
            "diagnosis": random.choice([
                "Actual Viral Infection",
                "Migraine episode",
                "Gastrointestinal distress"
            ]),
            "recommendation": f"{random.randint(1,3)} days rest"
        }

    @staticmethod
    def generate_chat_log(sender: str, message: str):
        """Generate chat log dictionary."""
        return {
            "timestamp": datetime.now().strftime("%H:%M"),
            "sender": sender,
            "message": message,
        }
