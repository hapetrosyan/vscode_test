import datetime
import datetime
from scipy import stats
from re import sub
import misc_ops
import requests


mo = misc_ops.MiscOps()


resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo')

if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
resp_json = resp.json() # ['Time Series (Daily)']
# for todo_item in resp.json():
    # print('{} {}'.format(todo_item['id'], todo_item['login']))
    # print(todo_item)

resp_metadata = resp_json['Meta Data']
resp_time_series = resp_json['Time Series (Daily)']


for key, value in resp_time_series.items():
    print(key, value)