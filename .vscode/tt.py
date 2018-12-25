import datetime
import datetime
from scipy import stats
from re import sub
import misc_ops
import requests


mo = misc_ops.MiscOps()


resp = requests.get('https://api.github.com/users/hadley/orgs')

if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['login']))
    # print(todo_item)