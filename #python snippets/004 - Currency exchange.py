"""
    You know that feeling when a Russian oligarch keeps offering you bribes but
    since they are in Rubles you can't really decide if it's worth it? Now you
    can find out! (It's also useful for when hotels report in different
    currencies, but who cares about that..) See the full documentation of the
    currency module here - https://80days.github.io/benchmark-tools/currency
"""

from eighty_tools import currency
RUB_bribes = [5000,7000,9000,7000,30000] # Вы говорите по-английски?
GBP_bribes = []

r = currency.Rates() # initialise the Rates class
for bribe in RUB_bribes:
	# exchange bribe from Rubles to Pounds and append to new list
	converted_bribe = r.exchange('RUB', 'GBP', bribe)
	GBP_bribes.append(converted_bribe)

print(GBP_bribes)
