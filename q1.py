# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  mat = np.zeros((len(portfolios), len(portfolios),), dtype=int)
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      a = np.zeros((16,), dtype=int)
      b = np.zeros((16,), dtype=int)
      p1 = portfolios[i]
      p2 = portfolios[j]
      for i in range(15,-1,-1):
        if (p1 - 2**i >= 0):
          p1 -= 2**i
          a[i] = 1
        if (p2 - 2**i >= 0):
          p2 -= 2**i
          b[i] = 1
      c = np.add(a, b)
      for i in range(len(c)):
        c[i] %= 2
      d = 0
      for i in range(15,-1,-1):
        d += c[i] * 2**(15-i)
      mat[i, j] = d
  value = np.max(mat)
  #index = np.where(mat == value) 
  return value

 
#portfolios = np.random.randint(65535, size=int(sys.argv[1]))
portfolios = np.array([31318, 60888, 13074, 22511, 55982, 17233, 44421, 47235, 48325, 9176])

a = question01(portfolios)
print a

#print portfolios

#value, index = max(portfolios)

#print "the max merged portfolio has a value of:", value, "and is created by the merging of portfolio", index[0][0] + 1, "and portfolio", index[1][0] + 1




