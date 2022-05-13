# This class is responsible for structuring the flight data:
#   - Basing on lists (with json objects) with information on desirable destinations and possible flights.
#   - We check if there are flights prices lower than maximum target price.
#   - Return list of json objects with flights info where price is lower than maximum target price.

class FlightData:
    """Return list with json objects containing info about flights where price is lower than maximum target price"""
    def __init__(self, my_destinations, my_flights):
        self.my_destinations = my_destinations
        self.my_flights = my_flights
        self.good_deals = []
        self.find_good_deals()

    # ----------------- FUNCTION COMPARES PRICES AND COMPOSES LIST WITH FLIGHTS -----------------#
    def find_good_deals(self):
        for destination in self.my_destinations:
            for flight in self.my_flights:
                if destination['iataCode'] == flight['cityCodeTo'] and destination['lowestPrice'] >= flight['price']:
                    self.good_deals.append(flight)
        return self.good_deals

    # ----------------- FUNCTION USED FOR TESTING PURPOSES ------------------------#
    def show_good_deals(self):
        for flight in self.good_deals:
            print(f"This is a good deal: to {flight['cityTo']} "
                  f"on {flight['local_departure']} will cost {flight['price']}")
