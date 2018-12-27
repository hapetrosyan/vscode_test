


a = {'1. open': '42.3400', '2. high': '33.333'}

for k, v in a.items():
    print(k, v)


a['open'] = a['1. open']
a['open'] = a.pop('1. open')

for k, v in a.items():
    print(k, v)