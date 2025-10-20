from flask import Blueprint, request, jsonify
from src.models.aqi_model import predict_aqi
from src.models.advisory_model import generate_advisory
from src.api.validators import validate_aqi_request

api_bp = Blueprint('api', __name__)

@api_bp.route('/predict-aqi', methods=['POST'])
def predict_aqi_route():
    data = request.get_json()
    if not validate_aqi_request(data):
        return jsonify({"error": "Invalid input data"}), 400
    
    parameters = data.get('parameters')
    aqi = predict_aqi(parameters)
    return jsonify({"predicted_aqi": aqi}), 200

@api_bp.route('/advisory', methods=['POST'])
def advisory_route():
    data = request.get_json()
    if not validate_aqi_request(data):
        return jsonify({"error": "Invalid input data"}), 400
    
    aqi = data.get('aqi')
    group = data.get('group')
    advisory = generate_advisory(aqi, group)
    return jsonify(advisory), 200