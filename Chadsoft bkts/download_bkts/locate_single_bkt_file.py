from extract_leaderboard_information import get_track_data
from path_manipulations import extract_path
from path_manipulations import adjust_path

base = "http://tt.chadsoft.co.uk"
working_url = "http://tt.chadsoft.co.uk/leaderboard/19/8C4EEED505F0862CBB490A0AC0BD334515895710/00.json"
broken_url = base + "/leaderboard/0D/CD19D287B6578A396C8A4EC77ACF0C633B5C75A8/01.json"

''' This function takes in the url to a specific track's leaderboard and returns the api path to the rkg
file for the track's bkt as well as a trimmed version of that path so the rkg file can be named appropriately
when downloaded. For every single track leaderboard, this function will be run, and then the ouput will be used
to use the download function to download the bkt.'''
def ghost_filepath(url): 
    lines = get_track_data(url)
    line = lines[-1] # The last split is where all the ghosts are
    rkgs = line.split(".rkg") # Splitting on .rkg, turns out this separates the leaderboard well by rank
    path = extract_path(rkgs[1]) + ".rkg" 
    bkt_path = base + path
    adjusted_path = adjust_path(path) # This is for the name of each file

    # This block is a (bandaid) fix for leaderborads that only have one ghost
    if adjusted_path[:-4].isalnum() == False:
        path = extract_path(rkgs[0]) + ".rkg"
        bkt_path = base + path
        adjusted_path = adjust_path(path)

    return bkt_path, adjusted_path

''' This is a function that I used to analyze and troubleshoot the extracted information from a track's leaderboard
specifically when a given track did not work. This function is not needed. '''
def examine_track(url):
      with open("api_data.txt", "w", encoding="utf-8") as outfile:
        lines = get_track_data(url)
        #for idx, line in enumerate(lines):
           # outfile.write(f"LINE: {idx}--------------------------------------------- \n {line} \n")
        line = lines[-1]
        rkgs = line.split(".rkg")
        for i, split in enumerate(rkgs):
            print(f"SPLIT {i}\n {split}\n------------------------------------------------\n")
        path = extract_path(rkgs[1]) + ".rkg"
        bkt_path = base + path
        adjusted_path = adjust_path(path)
        if adjusted_path[:-4].isalnum() == False:
            print("False!!!!")
            path = extract_path(rkgs[0]) + ".rkg"
            bkt_path = base + path
            adjusted_path = adjust_path(path)

        print(path, bkt_path, adjusted_path)