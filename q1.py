# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  if portfolios == []:
    return 0
  big = len(bin(max(portfolios))[2:])
  c = merge(bin(portfolios[0])[2:].zfill(big), bin(portfolios[1])[2:].zfill(big))
  d0 = c.index('0')
  d1 = c.index('1')
  index = [0,1]

  answer = int(c, 2)

  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)): 
      a = bin(portfolios[i])[2:].zfill(big)
      b = bin(portfolios[j])[2:].zfill(big)
      if d0 == 0:
        if a[:d1] != b[:d1]:
          c = merge(a, b)
          d0 = c.index('0')
          d1 = c.index('1')

          answer = int(c, 2)

        else:
          c = merge(a[d1:], b[d1:]).zfill(big)
          ans = int(c, 2)
          if ans > answer:
            d0 = c.index('0')
            d1 = c.index('1')

            answer = ans

      else:
        e = merge(a[:d0], b[:d0])
        f = '1'*(d0)
        if e == f:
          c = merge(a[d0:], b[d0:])
          c = f + c
          if '0' in c:
            ans = int(c, 2)
            if ans > answer:
              d0 = c.index('0')
              d1 = c.index('1')

              answer = ans

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