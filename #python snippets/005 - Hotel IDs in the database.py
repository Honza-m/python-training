# You don't need to go through all hotels to find the one you need
# Go to the database website, find the ID of the hotel
# and use the database module to retreive that ID only.
# https://80days.github.io/benchmark-tools/database

from eighty_tools import database
chosen_id = int(14)
chosen_hotel = database.Get("Hotels").get_one_by_id(chosen_id)
print(chosen_hotel['full_name'])

# You can also get a list of hotels by list of ids
chosen_ids = [14, 81, 79]
hotels = database.Get("Hotels").get_more_by_ids(chosen_ids)
for hotel in hotels:
	print(hotel['full_name'])
