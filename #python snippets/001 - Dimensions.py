"""
    Have you tried using dimensions?
"""

from eighty_tools import database, ga_query

all_hotels = database.Get("Hotels").get_all_in_benchmarking()

r = ga_query.Get(hotel_data=all_hotels[0], dimensions='ga:deviceCategory').get_handled_data(handler="pandas")

print(r)
