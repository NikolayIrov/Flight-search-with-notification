import requests

# This class is responsible for talking to the Google Sheet:
#     - Through sheety.co service we get destinations (name of the city) and maximum target price (in EURO) for the flight.
#     - With tequila.kiwi.com we get IATA code of destination cities.
#     - Class return a json object with destination data(city name, city code, maximum target price).
#     - Tequila token is a private variable.
#     - API end points are constant from nikolay.irov@gmail.com accounts.

class DataManager:
    """Return list with json objects containing info about desirable destinations"""

    def __init__(self, tequila_token):
        # ------------------SHEETY CODES API----------------------#
        SHEETY_END_POINT = 'https://api.sheety.co/09969855dd98f75fc94e61695734b2ab/flights/prices'
        destination_request = requests.get(url=SHEETY_END_POINT)
        self.destination_json = destination_request.json()['prices']

        # ----------------- IATA CODES API------------------------#
        TEQUILA_LOCATIONS_END_POINT = 'https://tequila-api.kiwi.com/locations/query'
        TEQUILA_APIKEY = {'apikey': tequila_token}

        # ------------------IATA CODES UPDATE----------------------#
        for item in self.destination_json:
            location_data = {
                'term': item['city'],
                'location_types': 'city'
            }
            iata_request = requests.get(url=TEQUILA_LOCATIONS_END_POINT, headers=TEQUILA_APIKEY, params=location_data)
            iata_request_json = iata_request.json()
            iata_code = iata_request_json['locations'][0]['code']
            item['iataCode'] = iata_code


