"""
    The ga_query module is used to download data from the Google Analytics API.
    But what can you do with that data?

    The module can return the data in a special data structure known as
    a Pandas DataFrame. This data structure (much like a list or a dictionary),
    has it's own special methods that make the handling of the data easier for
    us. For example, when printed, it looks like an excel table, and it can be
    easily downloaded to excel using the .to_excel() method. It can also
    quickly sum or average the data.

    The above snippet shows how to get the data in the pandas dataframe
    structure, and some very basic common operations you can do with it.
    However, pandas is a very powerful and large library, and hence I suggest
    you have a look at one of the tutorials to get to know this library better.
    I quite like this one:
    https://www.tutorialspoint.com/python_pandas/python_pandas_introduction_to_data_structures.htm
"""

#### GET DATA FROM GA AS A PANDAS DATAFRAME ####
from eighty_tools import database, ga_query, ga_tools
# Get hotel settings from the database
hotel = database.Get("Hotels").get_one_by_id(7)
# Generate customised hotel segments since hotel from the database
hotel_seg = ga_tools.get_segments_for_hotel(hotel)

# Create Google Analytics Query
q = ga_query.Get(hotel_data=hotel,
                 segments=hotel_seg['basic'], # Filters group account if necessary, get's rid of voucher traffic
                 metrics="ga:sessions, ga:users, ga:transactionRevenue",
                 dimensions="ga:deviceCategory")

# Get results as a Pandas dataframe
r = q.get_handled_data(handler='pandas')
df = r['0,0,0'] # Get the first response (see https://80days.github.io/benchmark-tools/ga_query#request-ids)

#### PANDAS DATAFRAME MANIPULATION ####
# http://pandas.pydata.org/pandas-docs/stable/
# Pandas is a library used to provide data structures that make it easy to work with data.
# Essentially, Pandas has a DataFrame object which looks to an extent like an Excel table.

# The ga_query.Get().get_handled_data() can return a pandas dataframe
print(type(df))

# This means you can use all the pandas methods on this object/table
# Print a summary of the dataframe
print('\nDESCRIBE')
print(df.describe())

# Print first 5 rows of the dataframe
print('\nHEAD')
print(df.head())

# Print last 5 rows of the dataframe
print('\nTAIL')
print(df.tail())

# Print a selected column (by column name)
print('\n[COLUMN NAME]')
print(df['ga:sessions'])
print()
print(df['ga:transactionRevenue'])

# Print more columns
print('\n[[MORE, COLUMNS]]')
print(df[['ga:sessions', 'ga:users']])

# Print a selected row (by index name)
print('\nROW BY NAME')
print(df.loc['mobile'])

# Print a selected row (by index number)
print('\nROW BY INDEX')
print(df.iloc[0])

# Combine row and column selection
print('\nROW AND COLUMN')
print(df.loc['mobile']['ga:transactionRevenue'])

# Get dataframe sum
print('\nSUM')
print(df.sum())

# Get dataframe mean
print('\nMEAN')
print(df.mean())

# Export to excel
print('\nEXPORT TO EXCEL')
# df.to_excel('C:/users/somefolder') # Change the filepath first then uncomment
