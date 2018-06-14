"""
Imagine this. Your client's luxury hotel in Wakanda is not doing great.
But you have a feeling that it might be connected to the recent geopolitical climate.

There is a great table on Wikipedia that shows Global Peace Index for all countries,
and you could use this to compare how does the performance of your hotel relate
to this. However, it's a big table that you wouldn't want to copy by hand.

That's where the pandas.read_html() function comes in. Provide it with a link
to the wikipedia page, and it will return all the tables on this page as
a DataFrame object. All you need to do is select the table you want, maybe
improve it a bit and save it to excel.

http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.read_html.html
"""


import pandas as pd

# Get the page that contains some tables
wiki_link = "https://en.wikipedia.org/wiki/Global_Peace_Index"

# Use pandas to scrape all the tables off the page, this will return a list
list_of_dataframes = pd.read_html(wiki_link) # Check out http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.read_html.html for more options
print(type(list_of_dataframes))

# Go through all the tables that we scraped
for df in list_of_dataframes:
    print(df.head()) # Use .head() to only print first 5 rows of the tables

# The table that we are interested got printed second
# Bearning in mind Python's 0-indexing, we get this table from the list
table = list_of_dataframes[1]

print(type(table)) # This is a pandas.DataFrame object that we can manipulate just like we saw in the previous snippet

# Printing out just this table
print(table.head())
# Notice that the table has no index, and no column names, just numbers.

# We can set columns to be the same as first row of the table, and then delete that row
table.columns = table.iloc[0]
table.drop(0, inplace=True) # inplace=True makes this work on the object without retourning a new onw
# Then we can set index using column name
print(table.head())
table.set_index('Country')

# Now that we have index and column names, we can dig in
print(table.iloc[[6,56],0:5])

# Or just export the whole thing to excel
# table.to_excel('D:/mypath/myfile.xlsx')
