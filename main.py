import requests
import time
import json
import csv
import pandas as pd


with open('ships.json') as json_file:
    ships = json.load(json_file)

vars_to_keep = ["POSIX", "name", "imo", "shipid", "lat", "lon"] 

# Headers to use in request
headers = {
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'Accept': '*/*',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'host': 'www.marinetraffic.com',
  'Cookie': 'SERVERID=app5nzs'
}

# Endpoint to request
endpoint = "https://www.marinetraffic.com/vesselDetails/latestPosition/shipid:"

# Request each ship
responses = [requests.request("GET", url = endpoint + ship['shipid'], headers=headers) for ship in ships]

# Extract json from response and add ship information
json_res = [{**{"POSIX": time.time()}, **ship, **response.json()} for ship, response in zip(ships, responses)]

# Filter the responses to keep only the variables of interest
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
json_filtered = [dictfilt(ship, vars_to_keep) for ship in json_res]

with open('out.jsonl', 'a') as f:
    for entry in json_filtered:
        json.dump(entry, f)
        f.write('\n')
        
df = pd.read_json ('out.jsonl')
df.to_csv ('out.csv', index = None)
           
