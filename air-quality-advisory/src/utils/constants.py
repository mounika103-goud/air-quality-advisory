# Constants for the Intelligent Air Quality Prediction and Health Advisory System

# Air Quality Index (AQI) Categories
AQI_CATEGORIES = {
    "Good": (0, 50),
    "Moderate": (51, 100),
    "Unhealthy for Sensitive Groups": (101, 150),
    "Unhealthy": (151, 200),
    "Very Unhealthy": (201, 300),
    "Hazardous": (301, 500)
}

# Health Advisory Messages
HEALTH_ADVISORIES = {
    "Good": "Air quality is considered satisfactory, and air pollution poses little or no risk.",
    "Moderate": "Air quality is acceptable; however, for some pollutants, there may be a moderate health concern for a very small number of people.",
    "Unhealthy for Sensitive Groups": "Members of sensitive groups may experience health effects. The general public is not likely to be affected.",
    "Unhealthy": "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
    "Very Unhealthy": "Health alert: everyone may experience more serious health effects.",
    "Hazardous": "Health warnings of emergency conditions. The entire population is more likely to be affected."
}

# API Configuration
API_URL = "http://localhost:5000/advisory"
TIMEOUT = 5  # seconds for API requests

# Other Constants
DEFAULT_LOCATION = "Unknown"
DEFAULT_AQI = 0