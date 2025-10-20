import pytest
from src.services.aqi_service import process_aqi_data
from src.services.advisory_service import generate_health_advisory

def test_process_aqi_data_valid():
    aqi_data = {'pm10': 50, 'pm2_5': 30, 'no2': 20}
    result = process_aqi_data(aqi_data)
    assert result['aqi'] is not None
    assert result['category'] in ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']

def test_process_aqi_data_invalid():
    aqi_data = {'pm10': -10, 'pm2_5': 30, 'no2': 20}
    with pytest.raises(ValueError):
        process_aqi_data(aqi_data)

def test_generate_health_advisory_good_aqi():
    aqi = 40
    advisory = generate_health_advisory(aqi)
    assert advisory == "Air quality is considered satisfactory, and air pollution poses little or no risk."

def test_generate_health_advisory_unhealthy_aqi():
    aqi = 150
    advisory = generate_health_advisory(aqi)
    assert advisory == "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."