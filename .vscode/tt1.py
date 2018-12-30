import requests
import json

symbol = 'AMZN'
request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=K2L959U20SZIKBDG'
resp = requests.get(request_link)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
resp_json = resp.json()

with open('result_'+symbol+'.json', 'w') as fp:
    json.dump(resp_json, fp)