
import matplotlib.pyplot as plt
import numpy as np
import get_data as d

dt = d.get_data()

proc_date = []

for row in dt:
    print(row[0])
    proc_date.append(row[0])


proc_date_set = set(proc_date)

print(sorted(proc_date_set))