"""
    This one is dedicated to Murdo who wondered whether he could just pull it
    all into an excel spreadsheet instead messing around the console.
    Yes we can!
"""
from eighty_tools import database, ga_query

# Get all hotels from database
all_hotels = database.Get("Hotels").get_all_in_benchmarking()

# Set up the query for one of the hotels
q = ga_query.Get(hotel_data=all_hotels[0])

# Get data in 'pandas' (excel-like format)
results = q.get_handled_data(handler="pandas")

# Notice that the data is returned in a dictionary, so you'll
# need to access the pandas part using the '0,0,0' key
print(results)

# Use .to_excel to create an excel file
results['0,0,0'].to_excel('results.xlsx')
