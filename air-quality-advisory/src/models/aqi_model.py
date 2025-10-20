class AQI:
    def __init__(self, value, category):
        self.value = value
        self.category = category

    def __repr__(self):
        return f"AQI(value={self.value}, category='{self.category}')"

    @staticmethod
    def categorize_aqi(value):
        if value <= 50:
            return "Good"
        elif value <= 100:
            return "Moderate"
        elif value <= 150:
            return "Unhealthy for Sensitive Groups"
        elif value <= 200:
            return "Unhealthy"
        elif value <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    @classmethod
    def from_value(cls, value):
        category = cls.categorize_aqi(value)
        return cls(value, category)