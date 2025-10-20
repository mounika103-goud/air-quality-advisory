from src.models.aqi_model import predict_aqi
from src.utils.constants import AQI_THRESHOLDS

class AQIService:
    def __init__(self):
        self.aqi_thresholds = AQI_THRESHOLDS

    def get_aqi_prediction(self, input_parameters):
        """
        Predicts the AQI based on the provided input parameters.
        """
        aqi = predict_aqi(input_parameters)
        return aqi

    def get_aqi_category(self, aqi):
        """
        Returns the AQI category based on the predicted AQI value.
        """
        for lower, upper, category in self.aqi_thresholds:
            if lower <= aqi <= upper:
                return category
        return "Unknown"