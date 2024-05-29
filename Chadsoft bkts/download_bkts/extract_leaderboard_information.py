import requests

''' This function takes in a url, which in this case should be the api url to 
a given track's leaderboard, and simply requests the information, and splits it. Due to
the formatting of the text, the splitting is quite convenient, as in all cases, the ghost
information needed is contained in the last split. This could be done more efficiently
but it is simple and it works, and it leaves the rest of the information around to work with if
desired.'''
def get_track_data(url):
  
  response = requests.get(url)

  if response.status_code == 200:
      lines = response.text.splitlines()
      return lines
  else:
    raise Exception("Error fetching data from API")