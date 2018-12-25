import datetime
import datetime
from scipy import stats
from re import sub
import misc_ops
import requests
from yahoo_finance import Share

mo = misc_ops.MiscOps()

print(mo.get_date_from_string('2018-01-14'))

# yahoo = Share('YHOO')
# print (yahoo.get_open())

# # resp = requests.get('https://api.github.com/users/hadley/orgs')
# resp = requests.get('link')
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# for todo_item in resp.json():
#     # print('{} {}'.format(todo_item['id'], todo_item['login']))
#     print(todo_item)