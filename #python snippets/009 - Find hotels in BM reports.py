"""
    Say you wanted to get a list of all the hotels in the London 5 Star set,
    so you could compare how many rooms do hotels in this set have on average.
    Doing this manually would take too long, because these reports can have
    hundreds of hotels. However, all of these sets are saved in the database,
    so all you need to do is to select the "BM_reports" table, get your report,
    get the hotel_ids associated with this report, and finally retrieve the
    hotels from the database using their hotel ids.
"""

>>> from eighty_tools import database
# Find the id of your report from the BM website, or use .get_all() instead to get the list of all the reports
>>> my_report = database.Get("BM_reports").get_one_by_id(7)
>>> print(my_report)
{
	'id': 7,
	'name': 'London - 5 Star',
	'frequency': 1,
	'currency': 'GBP',
	'type': 'Report,AdWords,Sessions_Index,Conver_Index,Ecom_Index,Speed,List,Glossary',
	'hotel_list': '26,14,323,16,27,19,25,377,101,15,18,105,20,23,112,17,21,24,106,22,399'
}
# Each report dict has a hotel_list key, with a string value.
>>> print(type(my_report['hotel_list']))
<class 'str'>
# This means we can use the .split method to split the string into a list, using commas as delimiters.
>>> hotel_ids = my_report['hotel_list'].split(',')
>>> print(hotel_ids)
['26', '14', '323', '16', '27', '19', '25', '377', '101', '15', '18', '105', '20', '23', '112', '17', '21', '24', '106', '22', '399']
# This is almost ready, but to get the hotel information from the databse, the ID needs to be an integer, not a string.
integer_hotel_ids = []
for each in hotel_ids:
	integer_hotel_ids.append(int(each))

# We can use these to get the full hotel information from the "Hotels" table
>>> selected_hotels = database.Get("Hotels").get_more_by_ids(integer_hotel_ids)
>>> print(selected_hotels)
[
	{
		'id': 26,
		'full_name': '11 Cadogan Gardens',
		'n_of_rooms': 56,
		...
	},
	...
]

# And finallly, to get the average number of rooms
>>> rooms = []
>>> for hotel in selected_hotels:
>>> 	rooms.append(hotel['n_of_rooms'])

# Import the numpy library and use it's mean function to get a mean of a list of numbers
>>> import numpy
>>> print(numpy.mean(rooms))
