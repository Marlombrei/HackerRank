from __future__ import division, print_function
import pandas.tseries
import numpy as np
import numpy.random as npr
import scipy as sp
import scipy.stats as scs
import scipy.optimize as sco
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import math

pd.set_option('display.width', 500)
pd.options.display.float_format = '{:,.4f}'.format
pd.options.display.max_rows = 10
np.set_printoptions(linewidth=200)

# a = int(11)
# b = int(5)
# 
# if 1<= a <=10**10 and 1<=b<=10**10:
#     print(a + b)
#     print(a - b)
#     print(a * b)

# N = int(5)
# if N > 0 and 1<=N<=20:
#     for i in range(N):
#         print(i**2)


year = int(2000)

def is_leap(y):
    # Write your logic here
    if 1900<= y <=10**5:
        leap = False
        if y%4 == 0:
            leap = True
            if y%100 == 0:
                leap = False
                if y%400 == 0:
                    leap = True
        return leap

print(is_leap(1992))




















































