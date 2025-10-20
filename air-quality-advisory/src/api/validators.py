from flask import request
from marshmallow import Schema, fields, ValidationError

class AQIValidator(Schema):
    aqi = fields.Int(required=True, validate=lambda n: n >= 0)
    location = fields.Str(required=True)

def validate_aqi_data(data):
    try:
        AQIValidator().load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    return None

class AdvisoryValidator(Schema):
    advisory_level = fields.Str(required=True)
    recommendations = fields.List(fields.Str(), required=True)

def validate_advisory_data(data):
    try:
        AdvisoryValidator().load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    return None