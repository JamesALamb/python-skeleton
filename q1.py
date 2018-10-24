# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  if portfolios == []:
    return 0
  big = len(bin(max(portfolios))[2:])
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)): 
      a = bin(portfolios[i])[2:].zfill(big)
      b = bin(portfolios[j])[2:].zfill(big)
      if answer < 2**(big-1):
        c = merge(a, b)
        d = c.index('0')
        c = int(c, 2)
        if (c > answer):

          answer = c

      else:
        e = merge(a[:d], b[:d])
        f = '1'*(d)
        if e == f:
          c = merge(a[d:], b[d:])
          c = f + c
          if '0' in c:
            d = c.index('0')

            answer = int(c, 2)

          else:

            answer = int(c, 2)

            return answer

  return answer


def merge(a, b):
  la = list(a)
  lb = list(b)
  la = [ int(x) for x in la ]
  lb = [ int(x) for x in lb ]
  c = np.add(la, lb)
  c = [ x % 2 for x in c ]
  c = [ str(x) for x in c ]
  c = ''.join(c)
  return c

portfolios = [1588038419, 1603264833, 2029937021, 713941009, 923957192, 1118942085, 59239954, 837238868, 753246235, 1403394345, 886500603, 1648810182, 1540165060, 1680351736, 1044516203, 1655352860, 1381992751]

answer = question01(portfolios)

print answer
