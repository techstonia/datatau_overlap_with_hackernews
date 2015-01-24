from compare import compare_to_hn
from parse_datatau import get_last_30_days_datatau
from util import remove_file_if_exists


if __name__ == '__main__':

  # delete
  remove_file_if_exists()

  # re-parse the data from the last 30 days
  get_last_30_days_datatau()

  # make comparisons
  compare_to_hn()