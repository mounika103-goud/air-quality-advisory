def validate_aqi(aqi):
    if not isinstance(aqi, (int, float)):
        raise ValueError("AQI must be a number.")
    if aqi < 0 or aqi > 500:
        raise ValueError("AQI must be between 0 and 500.")

def validate_group(group):
    valid_groups = [
        "Children",
        "Elderly",
        "People with respiratory or heart diseases",
        "Pregnant women"
    ]
    if group and group not in valid_groups:
        raise ValueError(f"Group must be one of the following: {', '.join(valid_groups)}")

def validate_request_data(data):
    if 'aqi' not in data:
        raise ValueError("Missing 'aqi' in request data.")
    validate_aqi(data['aqi'])
    if 'group' in data:
        validate_group(data['group'])