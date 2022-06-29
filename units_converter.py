from Calc import Calc

class UnitsConverter(Calc):
    def centimetersAndMeters(self, centimeters, meters):
        if centimeters == "" and meters == "":
            return 1
        elif centimeters.isnumeric() and meters.isnumeric():
            return 1
        elif centimeters == "":
            centimeters = 0
            return f"{float(meters)} meters is equals to {float(meters) * 100} centimeters"
        elif meters == "":
            meters = 0
            return f"{float(centimeters)} centimeters is equals to {float(centimeters) / 100} meters"

    def kilometersAndMeters(self, kilometers, meters):
        if kilometers == "" and meters == "":
            return 1
        elif kilometers.isnumeric() and meters.isnumeric():
            return 1
        elif kilometers == "":
            kilometers = 0
            return f"{float(meters)} meters is equals to {float(meters) / 1000} kilometers"
        elif meters == "":
            meters = 0
            return f"{float(kilometers)} kilometers is equals to {float(kilometers) * 1000} meters"

    def milesAndMeters(self, miles, meters):
        if miles == "" and meters == "":
            return 1
        elif miles.isnumeric() and meters.isnumeric():
            return 1
        elif miles == "":
            miles = 0
            return f"{float(meters)} meters is equals to {float(meters) / 1609.34} miles"
        elif meters == "":
            meters = 0
            return f"{float(miles)} miles is equals to {float(miles) * 1609.34} meters"