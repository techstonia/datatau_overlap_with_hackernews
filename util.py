import json
import os


TAU_DATA_PATH = './data/tau.csv'

# helpers for appending to .csv files
def update_file(item):
  with open(TAU_DATA_PATH, 'a') as csv_file:
    csv_file.write(str(item) + '\n')


# helpers for reading .csv files
def load_file():
  dicts = []

  with open(TAU_DATA_PATH, 'r') as csv_file:
    lines = csv_file.readlines()
    for line in lines:
      d = json.loads(line)
      dicts.append(d)

  return dicts


# helpers for deleting .csv files
def remove_file_if_exists():
  if os.path.exists(TAU_DATA_PATH):
    os.remove(TAU_DATA_PATH)