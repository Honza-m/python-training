"""
    @ana had a great idea for a loop exercise. Can you connect to the
    BM database and figure out how many BM clients we have in France?
    Try it out, and if you're stuck, here's a snippet to help you.
"""

from eighty_tools import database
all_hotels = database.Get("Hotels").get_all_in_benchmarking()

#check what info does one hotel dictionary include
	#[0] to get the first hotel in the list
	#.keys() to get the keys of the dict
print("These is the information available in the hotel dictionary:")
print(all_hotels[0].keys())
print("")

#Loop through all_hotels and save the ones where country == France to a new list
chosen_hotels = [] # new list
for hotel in all_hotels: # for loop
	if hotel['country'] == 'France': #['country'] to access item behind country key
		chosen_hotels.append(hotel) #if condition then append the n ew list with the hotel

#How many hotels did we get?
x = len(chosen_hotels) #len() returns length of an element
print("There are "+str(x)+" hotels in France")
print("")

#What are their names?
print("Full list of these hotels follows:")
for hotel in chosen_hotels:
	print(hotel['full_name'])
