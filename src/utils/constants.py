AQI_ADVISORY_TABLE = [
    (0, 50, "Good", "Air quality is considered satisfactory, and air pollution poses little or no risk."),
    (51, 100, "Moderate", "Air quality is acceptable; however, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."),
    (101, 150, "Unhealthy for Sensitive Groups", "Members of sensitive groups may experience health effects. The general public is less likely to be affected."),
    (151, 200, "Unhealthy", "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."),
    (201, 300, "Very Unhealthy", "Health alert: everyone may experience more serious health effects."),
    (301, 500, "Hazardous", "Health warnings of emergency conditions. The entire population is more likely to be affected."),
]

SENSITIVE_GROUPS = [
    "Children",
    "Elderly",
    "People with respiratory or heart diseases",
    "Pregnant women"
]


from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class AQILevel:
    category: str
    emoji: str
    description: str
    recommendations: List[str]


# Basic pollutant specs (units and threshold examples). These are illustrative only.
POLLUTANT_SPECS: Dict[str, Dict[str, Any]] = {
    'NO₂': {'unit': 'µg/m³', 'min': 0, 'max': 1000, 'default': 40.0, 'warning_threshold': 100, 'severe_threshold': 200, 'description': 'Nitrogen dioxide', 'health_effects': 'Irritation of airways; respiratory symptoms.'},
    'SO₂': {'unit': 'µg/m³', 'min': 0, 'max': 1000, 'default': 20.0, 'warning_threshold': 80, 'severe_threshold': 200, 'description': 'Sulfur dioxide', 'health_effects': 'Breathing difficulty for asthmatics; throat irritation.'},
    'CO': {'unit': 'mg/m³', 'min': 0, 'max': 100, 'default': 0.5, 'warning_threshold': 5, 'severe_threshold': 30, 'description': 'Carbon monoxide', 'health_effects': 'Reduces oxygen delivery to the body.'},
    'O₃': {'unit': 'µg/m³', 'min': 0, 'max': 1000, 'default': 30.0, 'warning_threshold': 100, 'severe_threshold': 180, 'description': 'Ozone', 'health_effects': 'Respiratory irritation and reduced lung function.'},
    'PM₁₀': {'unit': 'µg/m³', 'min': 0, 'max': 1000, 'default': 60.0, 'warning_threshold': 100, 'severe_threshold': 250, 'description': 'Particulate matter 10µm', 'health_effects': 'Aggravates respiratory illness.'},
    'PM₂.₅': {'unit': 'µg/m³', 'min': 0, 'max': 1000, 'default': 40.0, 'warning_threshold': 60, 'severe_threshold': 150, 'description': 'Fine particulate matter 2.5µm', 'health_effects': 'Penetrates deep into lungs and bloodstream.'},
    'NH₃': {'unit': 'µg/m³', 'min': 0, 'max': 10000, 'default': 10.0, 'warning_threshold': 400, 'severe_threshold': 1000, 'description': 'Ammonia', 'health_effects': 'Irritation to eyes and respiratory tract.'},
    'Pb': {'unit': 'µg/m³', 'min': 0, 'max': 10, 'default': 0.1, 'warning_threshold': 0.5, 'severe_threshold': 1.0, 'description': 'Lead', 'health_effects': 'Neurotoxin; long-term exposure harmful.'},
    'CO₂': {'unit': 'ppm', 'min': 0, 'max': 5000, 'default': 410.0, 'warning_threshold': 1000, 'severe_threshold': 5000, 'description': 'Carbon dioxide', 'health_effects': 'High levels cause drowsiness and headaches.'},
    'CH₄': {'unit': 'ppm', 'min': 0, 'max': 10000, 'default': 1.9, 'warning_threshold': 50, 'severe_threshold': 1000, 'description': 'Methane', 'health_effects': 'Asphyxiant at very high concentrations.'},
}


# Simple city modifiers to simulate different urban baselines
INDIAN_CITIES: Dict[str, Dict[str, Any]] = {
    # National and large metropolitan areas
    'Delhi': {'base_mult': 1.35, 'state': 'Delhi'},
    'Mumbai': {'base_mult': 1.05, 'state': 'Maharashtra'},
    'Bengaluru': {'base_mult': 0.95, 'state': 'Karnataka'},
    'Kolkata': {'base_mult': 1.10, 'state': 'West Bengal'},
    'Chennai': {'base_mult': 0.98, 'state': 'Tamil Nadu'},
    'Hyderabad': {'base_mult': 1.00, 'state': 'Telangana'},
    'Pune': {'base_mult': 0.95, 'state': 'Maharashtra'},
    'Ahmedabad': {'base_mult': 1.02, 'state': 'Gujarat'},
    'Jaipur': {'base_mult': 1.00, 'state': 'Rajasthan'},
    'Lucknow': {'base_mult': 1.15, 'state': 'Uttar Pradesh'},
    'Patna': {'base_mult': 1.20, 'state': 'Bihar'},
    'Bhopal': {'base_mult': 1.05, 'state': 'Madhya Pradesh'},
    'Surat': {'base_mult': 0.98, 'state': 'Gujarat'},
    'Vadodara': {'base_mult': 0.97, 'state': 'Gujarat'},
    'Nagpur': {'base_mult': 1.00, 'state': 'Maharashtra'},
    'Indore': {'base_mult': 0.99, 'state': 'Madhya Pradesh'},
    'Thiruvananthapuram': {'base_mult': 0.90, 'state': 'Kerala'},
    'Kochi': {'base_mult': 0.92, 'state': 'Kerala'},
    'Guwahati': {'base_mult': 1.10, 'state': 'Assam'},
    'Ranchi': {'base_mult': 1.05, 'state': 'Jharkhand'},
    'Bhubaneswar': {'base_mult': 0.98, 'state': 'Odisha'},
    'Dehradun': {'base_mult': 0.94, 'state': 'Uttarakhand'},
    'Chandigarh': {'base_mult': 0.93, 'state': 'Chandigarh'},
    'Coimbatore': {'base_mult': 0.91, 'state': 'Tamil Nadu'},
    'Mysore': {'base_mult': 0.88, 'state': 'Karnataka'},
}


def list_available_cities() -> List[str]:
    """Return a sorted list of available cities in INDIAN_CITIES."""
    return sorted(list(INDIAN_CITIES.keys()))


# Create AQI_LEVELS mapping and helper to get AQILevel
EMOJI_MAP = {
    'Good': '🟢',
    'Moderate': '🟡',
    'Unhealthy for Sensitive Groups': '🟠',
    'Unhealthy': '🔴',
    'Very Unhealthy': '🟣',
    'Hazardous': '⚫️',
}


def _build_aqi_levels():
    levels = {}
    for low, high, cat, desc in AQI_ADVISORY_TABLE:
        recommendations = [
            'Reduce prolonged outdoor exertion.' if cat not in ('Good',) else 'No special precautions needed.',
        ]
        levels[cat] = AQILevel(category=cat, emoji=EMOJI_MAP.get(cat, ''), description=desc, recommendations=recommendations)
    return levels


AQI_LEVELS = _build_aqi_levels()


def get_aqi_level(aqi: float) -> AQILevel:
    """Return an AQILevel dataclass for a numeric AQI value."""
    try:
        aqi_val = float(aqi)
    except Exception:
        return AQILevel(category='Unknown', emoji='❓', description='Invalid AQI', recommendations=[])
    for low, high, cat, desc in AQI_ADVISORY_TABLE:
        if low <= aqi_val <= high:
            return AQI_LEVELS.get(cat, AQILevel(category=cat, emoji='', description=desc, recommendations=[]))
    # If above table, return Hazardous
    return AQI_LEVELS.get('Hazardous', AQILevel(category='Hazardous', emoji='⚫️', description='Hazardous', recommendations=[]))


def predict_aqi(input_vector: List[float]) -> float:
    """Simple heuristic predictor: weighted sum of inputs normalized to 0-500 scale.

    Input order expected: [NO2, SO2, CO, O3, PM10, NH3]
    """
    weights = [0.8, 0.6, 0.2, 0.5, 1.2, 0.1]
    total = 0.0
    for v, w in zip(input_vector, weights):
        try:
            total += float(v) * w
        except Exception:
            total += 0.0
    # Normalize to AQI-like 0-500 range using a heuristic divisor
    aqi_val = total / 2.0
    if aqi_val < 0:
        aqi_val = 0.0
    if aqi_val > 500:
        aqi_val = 500.0
    return round(aqi_val, 1)


def generate_daily_trend(base: float, hours: int = 24):
    """Generate a simple synthetic daily trend (list of floats)."""
    import math
    trend = []
    for h in range(hours):
        # simple sinusoidal daily pattern + noise
        value = base * (1 + 0.2 * math.sin(2 * math.pi * h / 24))
        trend.append(max(0.0, value))
    return trend
