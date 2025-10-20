from datetime import datetime

class AdvisoryService:
    def __init__(self):
        self.advisories = {
            "Good": "Air quality is considered satisfactory, and air pollution poses little or no risk.",
            "Moderate": "Air quality is acceptable; however, for some pollutants there may be a concern for a very small number of people who are unusually sensitive to air pollution.",
            "Unhealthy for Sensitive Groups": "Members of sensitive groups may experience health effects. The general public is not likely to be affected.",
            "Unhealthy": "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
            "Very Unhealthy": "Health alert: everyone may experience more serious health effects.",
            "Hazardous": "Health warnings of emergency conditions. The entire population is more likely to be affected."
        }

    def get_advisory(self, aqi):
        if aqi <= 50:
            return self.advisories["Good"]
        elif aqi <= 100:
            return self.advisories["Moderate"]
        elif aqi <= 150:
            return self.advisories["Unhealthy for Sensitive Groups"]
        elif aqi <= 200:
            return self.advisories["Unhealthy"]
        elif aqi <= 300:
            return self.advisories["Very Unhealthy"]
        else:
            return self.advisories["Hazardous"]

    def log_advisory(self, aqi):
        advisory = self.get_advisory(aqi)
        timestamp = datetime.now().isoformat()
        with open("advisory_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} - AQI: {aqi}, Advisory: {advisory}\n")
        return advisory