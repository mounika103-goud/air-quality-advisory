import numpy as np

class AQIModel:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def predict_aqi(self, parameters):
        """
        Predicts the AQI based on input parameters using a linear model.
        Parameters should be a dictionary with keys matching the coefficients.
        """
        if not all(param in parameters for param in self.coefficients.keys()):
            raise ValueError("Missing parameters for AQI prediction.")

        aqi = sum(self.coefficients[param] * parameters[param] for param in self.coefficients)
        return self._scale_aqi(aqi)

    def _scale_aqi(self, aqi):
        """
        Scales the AQI value to fit within the standard AQI range.
        """
        return max(0, min(aqi, 500))

# Example usage
if __name__ == "__main__":
    coefficients = {
        'pm10': 0.5,
        'pm2_5': 0.7,
        'no2': 0.3,
        'o3': 0.2
    }
    model = AQIModel(coefficients)
    parameters = {
        'pm10': 100,
        'pm2_5': 50,
        'no2': 30,
        'o3': 40
    }
    predicted_aqi = model.predict_aqi(parameters)
    print(f"Predicted AQI: {predicted_aqi}")