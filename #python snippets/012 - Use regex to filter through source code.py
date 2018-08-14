import re
import requests
from eighty_tools import database

hotels = database.Get("Hotels").get_all_in_benchmarking()

clients = []
for hotel in hotels:
    if hotel['client'] == 1: clients.append(hotel['website_url'])

def get_tags(url):
    source_code = requests.get(url).text

    og_regex = r"<meta property=\"og:.*?>"
    tw_regex = r"<meta name=\"twitter:.*?>"

    og_matches = re.findall(og_regex, source_code, flags=re.IGNORECASE)
    tw_matches = re.findall(tw_regex, source_code, flags=re.IGNORECASE)

    res = url + " \nFACEBOOK - " + ", ".join(og_matches) + " \nTWITTER - " + ", ".join(tw_matches) + "\n\n"
    return res

results = ""
for i, url in enumerate(clients):
    try:
        print(f"{url} - {i+1}/{len(clients)}")
        results = results + get_tags(url)
    except Exception as e:
        pass
        print(f"ERROR at {url} - {e}")

with open('ogtags.txt','w') as file:
    file.write(results)
