from urllib.request import urlopen
import json
import csv

EXAMPLE_DIRECTORY = "aasa_examples"
URLS_CSV = 'urls.csv'

def main():
  with open(URLS_CSV) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      base_url = row['url']
      aasa_url = f'{base_url}/apple-app-site-association'
      try:
        download_file(url=aasa_url, name=row["name"])
      except Exception as ex: 
        print(f'There was an error downloading the file. URL:{aasa_url} exception: {ex}')

def download_file(url,name):
  try:
    print(f'Downloading {url}')
    response = urlopen(url)
  except Exception as ex:
    raise ex
  try:
    data_json = json.loads(response.read())
    file_name = f'{EXAMPLE_DIRECTORY}/{name}.json'
    with open(file_name,"w") as write_file:
      json.dump(data_json, write_file, indent=4)
    print(f'Saved to {file_name}')
  except:
    raise Exception("Invalid file format")
main()
