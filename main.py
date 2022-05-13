# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# ----------------- PERSONAL DATA ------------------------#
TEQUILA_TOKEN = 'zKCjirVEs9SnIdsT4FQGOAe-Oj1GT5aq'
HOST = 'smtp.gmail.com'
USER = 'nikolay.irov@gmail.com'
PASS = None

# ----------------- SEARCH AND NOTIFICATION ------------------------#
my_destinations = DataManager(TEQUILA_TOKEN)  # Get destination info (list of json)
my_flights = FlightSearch(TEQUILA_TOKEN,
                          my_destinations.destination_json)  # Get flights info for each destination (list of json)
my_good_deals = FlightData(my_destinations.destination_json,
                           my_flights.flights_json)  # # Select flights which suits criteria  (list of json)
my_notification = NotificationManager(HOST, USER, PASS, my_good_deals.good_deals)  # Compose message with flights info
# my_notification.notification() """Send message (won't work without email pass)"""
my_notification.show_notification()  # To show code performance message is printed on the screem
