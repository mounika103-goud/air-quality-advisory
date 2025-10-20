def test_get_aqi_category_and_advice():
    from src.models.aqi_model import get_aqi_category_and_advice

    assert get_aqi_category_and_advice(30) == ("Good", "Air quality is considered satisfactory, and air pollution poses little or no risk.")
    assert get_aqi_category_and_advice(75) == ("Moderate", "Air quality is acceptable; however, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.")
    assert get_aqi_category_and_advice(120) == ("Unhealthy for Sensitive Groups", "Members of sensitive groups may experience health effects. The general public is less likely to be affected.")
    assert get_aqi_category_and_advice(180) == ("Unhealthy", "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.")
    assert get_aqi_category_and_advice(250) == ("Very Unhealthy", "Health alert: everyone may experience more serious health effects.")
    assert get_aqi_category_and_advice(400) == ("Hazardous", "Health warnings of emergency conditions. The entire population is more likely to be affected.")
    assert get_aqi_category_and_advice(600) == ("Unknown", "AQI value out of range. Please check the input.")

def test_get_custom_advisory():
    from src.models.advisory_model import get_custom_advisory

    assert get_custom_advisory(30) == {
        "aqi_category": "Good",
        "advice": "Air quality is considered satisfactory, and air pollution poses little or no risk.",
        "group": "General"
    }
    assert get_custom_advisory(120, "Children") == {
        "aqi_category": "Unhealthy for Sensitive Groups",
        "advice": "Members of sensitive groups may experience health effects. The general public is less likely to be affected. Children should consider limiting outdoor exertion, wearing masks, and staying indoors if possible.",
        "group": "Children"
    }
    assert get_custom_advisory(180, "Elderly") == {
        "aqi_category": "Unhealthy",
        "advice": "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects. Elderly should consider limiting outdoor exertion, wearing masks, and staying indoors if possible.",
        "group": "Elderly"
    }
    assert get_custom_advisory(75, "Pregnant women") == {
        "aqi_category": "Moderate",
        "advice": "Air quality is acceptable; however, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.",
        "group": "Pregnant women"
    }