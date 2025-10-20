from flask import Blueprint, request, jsonify
from src.services.aqi_service import process_aqi_data
from src.services.advisory_service import generate_advisory

api = Blueprint('api', __name__)

@api.route('/advisory', methods=['POST'])
def advisory():
    data = request.json
    if not data or 'aqi' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    aqi_value = data['aqi']
    advisory = generate_advisory(aqi_value)
    return jsonify({'advisory': advisory}), 200

@api.route('/aqi', methods=['POST'])
def aqi():
    data = request.json
    if not data or 'location' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    location = data['location']
    aqi_data = process_aqi_data(location)
    return jsonify({'aqi_data': aqi_data}), 200