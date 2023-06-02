class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data, stop_over=0):
        self.stop_over = stop_over
        self.routes = [routes for routes in data["route"][:stop_over + 2]]
        self.departure_route = self.routes.pop(0)
        self.return_route = self.routes.pop()
        self.cityTo = self.return_route["cityFrom"]
        self.cityCodeTo = self.return_route["cityCodeFrom"]
        self.price = data["price"]
        self.departure_time = self.departure_route["utc_departure"].split("T")
        self.return_time = self.return_route["utc_departure"].split("T")
