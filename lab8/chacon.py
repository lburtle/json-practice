#!/usr/bin/python3

import json

def extract_repo_data(filename, num_lines=5):
  with open(filename, 'r') as f:
    data = json.load(f)

  with open('chacon.csv', 'w') as csv_file:
    for i in range(num_lines):
      repo = data[i]
      line = f"{repo['name']},{repo['html_url']},{repo['updated_at']},{repo['visibility']}\n"
      csv_file.write(line)

extract_repo_data('data/schacon.repos.json', 5)
