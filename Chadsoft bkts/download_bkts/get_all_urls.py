import requests
import re

''' This function will extract the api path for every custom track leaderboard.
At first, the extracted information is a large blob of text with the links inbetween,
so I had to run the extract_urls function which uses regular expressions to locate
and store the api paths. '''
def all_leaderboard_urls(url):
    response = requests.get(url)

    if response.status_code == 200:
        all_urls = extract_urls(response.text)
        return all_urls
    else:
        raise Exception("Error fetching data from API")
    
''' This function uses a regular expression specifically
made to find the leaderboard api paths. '''
def extract_urls(text):

    # /leaderboard/2 digit hex/lots of hex/2 digit.json
    pattern = r"/leaderboard/[A-F0-9]{2}/[A-F0-9]+/\d{2}\.json"

    # This stores all of the paths in a list
    matches = re.findall(pattern, text)

    return matches