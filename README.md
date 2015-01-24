# Exploring the overlap between datatau.com and hackernews stories
A simple and naive check of how many datatau.com links already have been posted on news.ycombinator.com.

##Basic usage
Run `run_em_all.py` for reproducing the results. This might take some time as re-parsing the sites is needed.

##Results
By default the script downloads last 30 days of links posted on datatau.com. At the time of writing there was 53.1% of overlap. Meaning that a bit more than half of the links present on datatau were also posted on hackernews. That's not surprising as hackernews gets lots of link submissions per month.

##Details
* `parse_tau.py` obtains links from datatau.com and stores them to ./data/tau.csv.
* `compare.py` loads the tau.csv and gets the percentage of overlapping stories. It uses [hn.algolia.com api](https://hn.algolia.com/api) and runs a search query for each datatau link and finds whether the link already is present on hackernews or not. 

##Why I believe the results are reliable?
I also used a different methodology. I downloaded last 30 days of stories from both sites and determined whether each datatau story url was contained in the set of hackernews stories (a bit less than 20 thousand links). The results were about the same, although the overlapping percentage was bit lower. I guess this is due to fact that stories on hackernews seem to appear in real time as opposed to datatau where it might take some time for a story to be submitted.   

P.S. I didn't like the second methodology as much as it was messy and thus don't include the scripts here.