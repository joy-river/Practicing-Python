class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.num_routes = int(len(data["route"]) / 2)
        self.departure_route = data["route"][0]
        self.return_route = data["route"][self.num_routes]
        self.flyFrom = data["flyFrom"]
        self.flyTo = data["flyTo"]
        self.cityTo = data["cityTo"]
        self.cityCodeTo = data["cityCodeTo"]
        self.price = data["price"]
        self.departure_time = self.departure_route["utc_departure"].split("T")
        self.return_time = self.return_route["utc_departure"].split("T")
