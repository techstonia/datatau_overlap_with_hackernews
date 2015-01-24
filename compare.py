"""
Loads datatau.com links from ./data folder and for each link
runs a search query against hackernews API for
checking whether the datatau link has posted on hackernews.

NB! If there's no tau.csv file, then run parse_datatau.py first.
"""

import json
import urllib2
from util import load_file


API_QUERY_TEMPLATE = "http://hn.algolia.com/api/v1/search?tags=story&query=%s"


def link_in_content(json_str, link):
  for hit in json.loads(json_str)['hits']:
    if hit['url'] == link:
      return True
  return False


def compare_to_hn():
  tau_stories = load_file()

  for i, tau_story in enumerate(tau_stories):
    tau_story['hn_has_it'] = False

    link = tau_story['link']
    print "Checking overlap. %s/%s %s" % (i, len(tau_stories), link)

    try:
      query_link = API_QUERY_TEMPLATE % link
      content = urllib2.urlopen(query_link).read()

      if link_in_content(content, link):
        tau_story['hn_has_it'] = True
    except urllib2.HTTPError:
      pass

  stat = sum([tau_story['hn_has_it'] for tau_story in tau_stories])/float(len(tau_stories))

  print ("\nChecked the last 30 days and"
         "%.1f%% of the stories on datatau "
         "have been featured on hackernews already" % (stat * 100))


if __name__ == '__main__':
  compare_to_hn()