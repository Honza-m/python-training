""" Essentially, an API is a web page that returns information in a nice
    machine-readable format. We use a number of APIs for benchmarking and
    other projects, but there are APIs for almost anything. For example -
    I'm sure you've all been wondering when is Jan's name day. There's an API
    for that. Every public API you will use will have a documentation that
    describes exactly what info you need to provide and what info it can
    provide back. The easiest way of making a request to an API is to use
    Python's requests library. Check the snippet and try it out!
"""

# Import the requests library that the script will use to communicate with the API
# I recommend having a look at it's documentation at some point, as some APIs require some more advanced features of the library - http://docs.python-requests.org/en/master/
import requests

# We'll use the abalin.net API to get our nameday information
# Before going further, check the documentation to see what the API provides - https://api.abalin.net

# We want to search nameday by name, so we set the appropriate endpoint
api_endpoint = "https://api.abalin.net/get/getdate"

# As you can see from the docs, there are two parameters that you need to provide - name that you are searching for, and a calendar (as each country has different name days)
# You can do this by creating a dictionary with parameter names as keys, and the information as values.
parameters = {
	'name': 'Jan',
	'calendar': 'cz'
}

# Now that we're all set, let's make the request using the requests library
# This is Python's equivalent to you typing this url in your browser - https://api.abalin.net/get/getdate?name=Jan&calendar=cz
response = requests.get(api_endpoint, params=parameters)

# The library will return a special response object
# Since the documentation says the API returns JSON strings, we can access these using the response objects' .json() method
result = response.json()
print(result)
