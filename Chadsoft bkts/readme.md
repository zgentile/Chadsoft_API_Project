The purpose of this project is to download all of the ct bkts automatically instead of having to
download all of them manually yourself. I have downloaded them all manually myself before
and it takes a lot of time and is very boring.

The only file that needs to be run is download_all_ghosts (which is brought into __main__.py). The rest are modules. 

The ghosts will all be downloaded into a 'ghosts' folder. All you would need to do is extract
the folder and merge it with your ghosts folder on your sd card. Note that unfortunately the 
names of the rkg files are not informative for us, as they are just the paths to the file which 
if I remember correctly is some sort of random hex identifier to ensure uniqueness. However,
thankfully the game knows what track each rkg file corresponds to! They will not go inside the folder
for each track, they will sit outside, but they will load correctly onto the tracks.

The next step for this project is to use more broad and advanced methods to locate the rkg files
instead of tuning it specifically around the bizarre structure of the api responses. The method that is
currently used is prone to malfunction if anything changes or more unique cases show up. As of right now,
the only thing that gave me trouble was leaderboards that had one ghost. I made a bandaid solution for that,
but I expect that even that will probably fail in future cases if there is something else also different about
that leaderboard. Also, I haven't looked into this all that much, but perhaps html scraping with something like
beautiful soup would be a better approach. I did this project as a way to get experience using apis, requests, and os.
I think something in the direction of AI or NLP will work better but that is a more advanced approach that I would probably need to put much more time into than I put into this.

Also, perhaps most importantly, I want this to be something that people can easily use. Obviously,
now it only works with python in a terminal, and I would imagine that most are not familiar with this.
I know there are loads of ways to do this, I need to learn how. 

Another thing I am curious about is cloning the structure of the ctgp ghosts folder into the the ghosts folder
here so that ghosts go in the correct folder. Perhaps it would be nice to also find a way to name the files in the same
exact way that chadsoft does. I don't think this would be too hard but I also don't think it matters. Anyway, in order to accomplish getting all of the ghosts from this into their proper folders, I would need to make a tool that goes into the rkg files and finds whatever information that the game/ctgp finds to designate it to a track. Not only would this help this tool, but it would also help downloads from the chadsoft website as well, as those ghosts are not sent to any folders.

Yeah, I didn't make any tests, I just kinda used lots of trial and error and checked that everything worked. It seems to work, but in the final product I will have tests.

I can't tell if it's because of this or not, but I think the ghosts may have slowed down the time it takes to load
a given track's ghosts in the game, by a lot. This is just suspicion though.

