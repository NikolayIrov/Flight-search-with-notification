import requests, datetime

# ----------------- CALCULATING DATES ------------------------#
today = datetime.datetime.today()
day = datetime.timedelta(days=1)
tomorrow = today + day
tommorow_str = tomorrow.strftime('%d/%m/%Y')
month6 = tomorrow + datetime.timedelta(days=180)
month6_str = month6.strftime('%d/%m/%Y')

# This class is responsible for talking to the Flight Search API:
#      - Desirable destinations from DataManager in list (with json objects) format are taken as input
#      - With tequila.kiwi.com we get 1 best price ticket for desirable destinations in form of json object.
#      - Departure set to London
#      - Possible dates are set for period: tommorow + 6 months (180 days)
#      - Tequila token is a private variable.
#      - API end points are constant from nikolay.irov@gmail.com accounts.

class FlightSearch:
    """Return list with json objects containing info about selected flights """

    def __init__(self, tequila_token, destinations):
        # ----------------- FLIGTH SEARCH API------------------------#
        TEQUILA_SEARCH_END_POINT = 'https://tequila-api.kiwi.com/v2/search'
        TEQUILA_APIKEY = {'apikey': tequila_token}
        self.destinations = destinations

        # ----------------- FLIGTH SEARCH------------------------#
        self.flights_json = []
        for destination in destinations:
            search_data = {
                'fly_from': 'LON',
                'fly_to': destination['iataCode'],
                'date_from': tommorow_str,
                'date_to': month6_str,
                'flight_type': 'oneway',
                'one_for_city': 1
            }
            flight_request = requests.get(url=TEQUILA_SEARCH_END_POINT, headers=TEQUILA_APIKEY, params=search_data)
            self.flights_json.append(flight_request.json()['data'][0])

        # ----------------- FUNCTION USED FOR TESTING PURPOSES ------------------------#

    def show_flights(self):
        for flight in self.flights_json:
            print(f"To {flight['cityTo']} on {flight['local_departure']} will cost {flight['price']}")
