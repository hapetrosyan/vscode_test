# import datetime
# from scipy import stats
# from re import sub
# import misc_ops
import requests
import data_ops

do = data_ops.DataOps()
# mo = misc_ops.MiscOps()


# resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SAVE&apikey=K2L959U20SZIKBDG')

# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# resp_json = resp.json() # ['Time Series (Daily)']
# # for todo_item in resp.json():
#     # print('{} {}'.format(todo_item['id'], todo_item['login']))
#     # print(todo_item)

# resp_metadata = resp_json['Meta Data']
# resp_time_series = resp_json['Time Series (Daily)']

symbol_dict = do.get_alphavantage_100_days_dict('SAVE')

for key, value in symbol_dict.items():
    print(key, value)
