from src.utils.constants import SENSITIVE_GROUPS, AQI_ADVISORY_TABLE

def get_aqi_category_and_advice(aqi: float):
    for lower, upper, category, advice in AQI_ADVISORY_TABLE:
        if lower <= aqi <= upper:
            return category, advice
    return "Unknown", "AQI value out of range. Please check the input."

def get_custom_advisory(aqi: float, group: str = None):
    category, advice = get_aqi_category_and_advice(aqi)
    if group and group in SENSITIVE_GROUPS and aqi >= 101:
        advice += f" {group} should consider limiting outdoor exertion, wearing masks, and staying indoors if possible."
    return {
        "aqi_category": category,
        "advice": advice,
        "group": group or "General"
    }