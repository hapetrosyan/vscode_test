
from scipy import stats
import numpy as np
import datetime
import get_data

print(get_data.get_data())

# x = np.random.random(10)
# y = np.random.random(10)

# day1 = datetime.date(2018,1,1)
# day2 = datetime.date(2018,1,2)
# day3 = datetime.date(2018,1,3)

day1 = 20180101
day2 = 20180202
day3 = 20180303

x = [day1,day2,day3]
y = [20,40,20]

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print ('slope: ',slope)
print ('intercept: ',intercept)
print ('r_value: ',r_value)
print ('p_value: ',p_value)
print ('std_err: ',std_err)

