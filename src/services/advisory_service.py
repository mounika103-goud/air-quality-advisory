def generate_health_advisory(aqi, group):
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

    for lower, upper, category, advice in AQI_ADVISORY_TABLE:
        if lower <= aqi <= upper:
            if group in SENSITIVE_GROUPS and aqi >= 101:
                advice += f" {group} should consider limiting outdoor exertion, wearing masks, and staying indoors if possible."
            return {
                "aqi_category": category,
                "advice": advice,
                "group": group or "General"
            }
    return {
        "aqi_category": "Unknown",
        "advice": "AQI value out of range. Please check the input.",
        "group": group or "General"
    }