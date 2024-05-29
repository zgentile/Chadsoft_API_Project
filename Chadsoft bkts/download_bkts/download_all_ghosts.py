from download_single_bkt import download

from get_all_urls import all_leaderboard_urls

from locate_single_bkt_file import ghost_filepath

def main():
    base = "http://tt.chadsoft.co.uk" # every url will start with this, so we can just concatenate onto it

    leaderboards_url = "http://tt.chadsoft.co.uk/ctgp-leaderboards.json" # this is where the api url for every ct leaderboard can be found

    leaderboards = all_leaderboard_urls(leaderboards_url) # finds every single leaderboard api url and stores them in a list

    ''' Iterate over every single ct leaderboard, and download the bkt for each one. I'm enumerating
    just to make sure that it runs the correct amount of times, which as of 5/29/24 would be 300 times (0-299). 
    The print statement isn't necessary, but it serves as a pseudo progress tracker. This in total takes around 25
    minutes to run, which is a while, but is already a lot better and less mundane than downloading them all manually. Around 13
    ghosts per minute for a total of 300 ghosts. '''
    for idx, leaderboard in enumerate(leaderboards):
        print(idx, leaderboard)
        path, filename = ghost_filepath(base + leaderboard)
        download(path, filename)