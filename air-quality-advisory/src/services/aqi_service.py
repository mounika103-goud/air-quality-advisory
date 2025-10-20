from src.models.aqi_model import AQIModel
from src.utils.constants import AQI_THRESHOLDS

class AQIService:
    def __init__(self):
        self.aqi_model = AQIModel()

    def process_aqi_data(self, aqi_data):
        # Validate and process the incoming AQI data
        if not self.validate_aqi_data(aqi_data):
            raise ValueError("Invalid AQI data")

        # Update the AQI model with the new data
        self.aqi_model.update_data(aqi_data)

        # Return the processed AQI data
        return self.aqi_model.get_data()

    def validate_aqi_data(self, aqi_data):
        # Check if the AQI data is within the defined thresholds
        return AQI_THRESHOLDS['min'] <= aqi_data <= AQI_THRESHOLDS['max']