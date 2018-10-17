# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  #mat = np.zeros((len(portfolios), len(portfolios),), dtype=int)
  answer = 0
  index = [0,0]
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
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
      #for k in range(len(c)):
        #c[k] %= 2
      d = 0
      for k in range(16):
        if (c[k] == 1):
          d += c[k] * 2**(15-k)
      if (d > answer):
        answer = d
        index = [i,j]
      #mat[i, j] = d
  #index = np.where(mat == value) 
  #answer = np.max(mat)
  return answer