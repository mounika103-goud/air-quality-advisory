from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    TESTING = os.getenv('TESTING', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    API_KEY = os.getenv('API_KEY', 'your_api_key')
    AQI_THRESHOLD = {
        "good": 50,
        "moderate": 100,
        "unhealthy_sensitive": 150,
        "unhealthy": 200,
        "very_unhealthy": 300,
        "hazardous": 500
    }
    SENSITIVE_GROUPS = [
        "Children",
        "Elderly",
        "People with respiratory or heart diseases",
        "Pregnant women"
    ]