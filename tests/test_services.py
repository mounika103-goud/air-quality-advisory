def test_aqi_prediction():
    from src.models.aqi_model import predict_aqi

    # Test cases for AQI prediction
    test_cases = [
        ({"param1": value1, "param2": value2}, expected_aqi1),
        ({"param1": value3, "param2": value4}, expected_aqi2),
    ]

    for inputs, expected in test_cases:
        result = predict_aqi(**inputs)
        assert result == expected, f"Expected {expected}, but got {result}"

def test_health_advisory():
    from src.models.advisory_model import generate_advisory

    # Test cases for health advisory generation
    test_cases = [
        (50, "Good", "Air quality is considered satisfactory."),
        (150, "Unhealthy for Sensitive Groups", "Members of sensitive groups may experience health effects."),
    ]

    for aqi, expected_category, expected_advice in test_cases:
        category, advice = generate_advisory(aqi)
        assert category == expected_category, f"Expected category {expected_category}, but got {category}"
        assert expected_advice in advice, f"Expected advice to contain '{expected_advice}', but got {advice}"