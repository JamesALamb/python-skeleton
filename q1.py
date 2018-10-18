# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
        a = binary(portfolios[i])
        b = binary(portfolios[j])
        if ( answer >= (2**15 + 2**14 + 2**13 + 2**12 + 2**11) ):
          if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]) and (a[4] != b[4]):
            d = merge(a, b)
            if (d > answer):
              answer = d
        elif ( answer >= (2**15 + 2**14 + 2**13 + 2**12) ):
          if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]):
            d = merge(a, b)
            if (d > answer):
              answer = d
        elif ( answer >= (2**15 + 2**14 + 2**13) ):
          if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]):
            d = merge(a, b)
            if (d > answer):
              answer = d
        elif ( answer >= (2**15 + 2**14) ):
          if (a[0] != b[0]) and (a[1] != b[1]):
            d = merge(a, b)
            if (d > answer):
              answer = d
        elif ( answer >= 2**15 ):
          if (a[0] != b[0]):
            d = merge(a, b)
            if (d > answer):
              answer = d
        else:
          d = merge(a, b) 
          if (d > answer):
            answer = d
  return answer

def binary(decimal):
  # get binary list from deciamal value
  binary = np.zeros((16,), dtype=int)
  for i in range(15,-1,-1):
    if (decimal - 2**i >= 0):
      decimal -= 2**i
      binary[15-i] = 1
  return binary

def merge(a, b):
  c = np.add(a, b)
  d = 0
  for i in range(len(c)):
    if (c[i] == 1):
      d += c[i] * 2**(15-i)
  return d
