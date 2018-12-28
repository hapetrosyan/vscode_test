import pandas as pd
import collections



d = {2: 'a', 1 :'b', 3: 'c'}

od = collections.OrderedDict(sorted(d.items()))


print(d)

print(od.__dict__())