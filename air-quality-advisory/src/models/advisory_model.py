class AdvisoryModel:
    def __init__(self, aqi_level):
        self.aqi_level = aqi_level
        self.advisory = self.generate_advisory()

    def generate_advisory(self):
        if self.aqi_level <= 50:
            return "Good: Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif self.aqi_level <= 100:
            return "Moderate: Air quality is acceptable; however, for some pollutants, there may be a moderate health concern for a very small number of people."
        elif self.aqi_level <= 150:
            return "Unhealthy for Sensitive Groups: Members of sensitive groups may experience health effects. The general public is not likely to be affected."
        elif self.aqi_level <= 200:
            return "Unhealthy: Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif self.aqi_level <= 300:
            return "Very Unhealthy: Health alert: everyone may experience more serious health effects."
        else:
            return "Hazardous: Health warnings of emergency conditions. The entire population is more likely to be affected."

    def get_advisory(self):
        return self.advisory