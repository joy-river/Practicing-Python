class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.flyFrom = data["flyFrom"]
        self.flyTo = data["flyTo"]
        self.cityTo = data["cityTo"]
        self.cityCodeTo = data["cityCodeTo"]
        self.price = data["price"]
        self.departure_time = data["route"][0]["utc_departure"].split("T")
        self.return_time = data["route"][1]["utc_departure"].split("T")