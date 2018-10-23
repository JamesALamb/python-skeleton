# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  print portfolios
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)): 
      if (portfolios[i] < 2**16 and portfolios[j] < 2**16):
        if ( answer >= (2**15 + 2**14 + 2**13 + 2**12 + 2**11) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]) and (a[4] != b[4]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**15 + 2**14 + 2**13 + 2**12) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**15 + 2**14 + 2**13) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**15 + 2**14) ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]) and (a[1] != b[1]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= 2**15 ):
          if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
            a = bin(portfolios[i])[2:].zfill(16)
            b = bin(portfolios[j])[2:].zfill(16)
            if (a[0] != b[0]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        else:
          a = bin(portfolios[i])[2:].zfill(16)
          b = bin(portfolios[j])[2:].zfill(16)
          c = merge(a, b) 
          if (c > answer):
  
            answer = c
  
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
  c = int(c, 2)
  return c
