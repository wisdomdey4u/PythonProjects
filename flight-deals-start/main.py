from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    'flight_cache',
    urls_expire_after={
        "*.sheet.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# ====================== Setup ==============================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()

# ======================= Set the Dates==============================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "ABV"

# ======================== Do a Flight Search ========================
for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code="KAN",
        destination_city_code="LOS",
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{sheet_data[0]['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price != "M/A" and cheapest_flight.price < sheet_data[0]['lowestPrice']:
        pprint(f"Lower price flight fount to {sheet_data[0]['city']}!")
        data_manager.update_lowest_price(sheet_data[0]['id'], cheapest_flight.price)
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )