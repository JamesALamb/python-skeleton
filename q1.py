# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
        if ( answer >= (2**15 + 2**14 + 2**13 + 2**12 + 2**11) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]) and (a[4] != b[4]):
              d = merge(a, b)
              if (d > answer):

                answer = d

        elif ( answer >= (2**15 + 2**14 + 2**13 + 2**12) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]):
              d = merge(a, b)
              if (d > answer):

                answer = d

        elif ( answer >= (2**15 + 2**14 + 2**13) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]):
              d = merge(a, b)
              if (d > answer):

                answer = d

        elif ( answer >= (2**15 + 2**14) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]):
              d = merge(a, b)
              if (d > answer):

                answer = d

        elif ( answer >= 2**15 ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]):
              d = merge(a, b)
              if (d > answer):

                answer = d

        else:
          a = bin(portfolios[i])[2:].zfill(16)
          b = bin(portfolios[j])[2:].zfill(16)
          d = merge(a, b) 
          if (d > answer):

            answer = d

  return answer



def merge(a, b):
  la = list(a)
  lb = list(b)
  la = [ int(x) for x in la ]
  lb = [ int(x) for x in lb ]
  c = np.add(la, lb)
  d = 0
  for i in range(len(c)):
    if (c[i] == 1):
      d += c[i] * 2**(15-i)
  return d
