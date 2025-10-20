from flask import json
from src.app import app

def test_post_advisory(client):
    response = client.post('/advisory', json={'aqi': 150})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'advisory' in data
    assert data['advisory'] == 'Unhealthy for sensitive groups'

def test_post_advisory_invalid_data(client):
    response = client.post('/advisory', json={'invalid_key': 150})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Invalid input data'

def test_post_advisory_no_data(client):
    response = client.post('/advisory', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'AQI data is required'