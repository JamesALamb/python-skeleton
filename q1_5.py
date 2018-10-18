# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np


# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
#  index = [0,0]
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      if ( answer < 2**15 ):
        a = np.zeros((16,), dtype=int)
        b = np.zeros((16,), dtype=int)
        p1 = portfolios[i]
        p2 = portfolios[j]
        for k in range(15,-1,-1):
          if (p1 - 2**k >= 0):
            p1 -= 2**k
            a[15-k] = 1
          if (p2 - 2**k >= 0):
            p2 -= 2**k
            b[15-k] = 1
        c = np.add(a, b)
        d = 0
        for k in range(16):
          if (c[k] == 1):
            d += c[k] * 2**(15-k)
        if (d > answer):
          answer = d
      elif ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
        a = np.zeros((16,), dtype=int)
        b = np.zeros((16,), dtype=int)
        p1 = portfolios[i]
        p2 = portfolios[j]
        for k in range(15,-1,-1):
          if (p1 - 2**k >= 0):
            p1 -= 2**k
            a[15-k] = 1
          if (p2 - 2**k >= 0):
            p2 -= 2**k
            b[15-k] = 1
        c = np.add(a, b)
        d = 0
        for k in range(16):
          if (c[k] == 1):
            d += c[k] * 2**(15-k)
        if (d > answer):
          answer = d
  return answer
