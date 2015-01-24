"""
Parses datatau.com links directly (without API) from the site.
"""

import json
import urllib2
from bs4 import BeautifulSoup
import time
from util import update_file


TAU_URL = 'http://www.datatau.com'

def parse_page(url):
  response = urllib2.urlopen(url)
  soup = BeautifulSoup(response)

  links = soup.findAll('td', {'class': 'title'})
  links = map(lambda td: td.findAll('a', href=True), links)
  links = filter(lambda l: len(l) >= 1, links)
  links = map(lambda l: l[0]['href'], links)

  links, next_page_link = links[:-1], links[-1]

  submit_times = soup.findAll('td', {'class': 'subtext'})
  submit_times = map(lambda td: td.contents[3], submit_times)
  submit_times = map(lambda s: s.replace('|', '').strip(), submit_times)

  assert len(links) == len(submit_times), "Number of submit times and links do not match."

  results = [{'link': link, 'submitted': submit_time} for link, submit_time in zip(links, submit_times)]
  results = [result for result in results if not result['link'].startswith('item?id=')]

  return {'next_page': next_page_link, 'results': results}


def get_last_30_days_datatau(exclude_time='31 days ago'):
  """
  :param exclude_time: get links newer than the parameter value
  """
  url = TAU_URL + '/newest'
  keep_going = True
  while keep_going:
    print "parsing %s" % url
    page_results = parse_page(url)

    for result in page_results['results']:
      if result['submitted'] != exclude_time and keep_going:
        update_file(json.dumps(result))
      else:
        keep_going = False

    possible_slash = '/' if page_results['next_page'][0] != '/' else ''
    url = TAU_URL + possible_slash + page_results['next_page']
    time.sleep(0.01)


if __name__ == '__main__':
  get_last_30_days_datatau()