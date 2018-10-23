# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  if portfolios == []:
    return 0
  big = len(bin(max(portfolios)))
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)): 
      if (portfolios[i] < 2**big and portfolios[j] < 2**big):
        if ( answer >= (2**(big-1) + 2**(big-2) + 2**(big-3) + 2**(big-4) + 2**(big-4)) ):
          if ( (portfolios[i] >= 2**(big-1) and portfolios[j] < 2**(big-1)) or (portfolios[j] >= 2**(big-1) and portfolios[i] < 2**(big-1)) ):
            a = bin(portfolios[i])[2:].zfill(big)
            b = bin(portfolios[j])[2:].zfill(big)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]) and (a[4] != b[4]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**(big-1) + 2**(big-2) + 2**(big-3) + 2**(big-4)) ):
          if ( (portfolios[i] >= 2**(big-1) and portfolios[j] < 2**(big-1)) or (portfolios[j] >= 2**(big-1) and portfolios[i] < 2**(big-1)) ):
            a = bin(portfolios[i])[2:].zfill(big)
            b = bin(portfolios[j])[2:].zfill(big)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]) and (a[3] != b[3]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**(big-1) + 2**(big-2) + 2**(big-3)) ):
          if ( (portfolios[i] >= 2**(big-1) and portfolios[j] < 2**(big-1)) or (portfolios[j] >= 2**(big-1) and portfolios[i] < 2**(big-1)) ):
            a = bin(portfolios[i])[2:].zfill(big)
            b = bin(portfolios[j])[2:].zfill(big)
            if (a[0] != b[0]) and (a[1] != b[1]) and (a[2] != b[2]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**(big-1) + 2**(big-2)) ):
          if ( (portfolios[i] >= 2**(big-1) and portfolios[j] < 2**(big-1)) or (portfolios[j] >= 2**(big-1) and portfolios[i] < 2**(big-1)) ):
            a = bin(portfolios[i])[2:].zfill(big)
            b = bin(portfolios[j])[2:].zfill(big)
            if (a[0] != b[0]) and (a[1] != b[1]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        elif ( answer >= (2**(big-1)) ):
          if ( (portfolios[i] >= 2**(big-1) and portfolios[j] < 2**(big-1)) or (portfolios[j] >= 2**(big-1) and portfolios[i] < 2**(big-1)) ):
            a = bin(portfolios[i])[2:].zfill(big)
            b = bin(portfolios[j])[2:].zfill(big)
            if (a[0] != b[0]):
              c = merge(a, b)
              if (c > answer):
  
                answer = c
  
        else:
          a = bin(portfolios[i])[2:].zfill(big)
          b = bin(portfolios[j])[2:].zfill(big)
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

#portfolios = [1588038419, 1603264833, 2029937021, 713941009, 923957192, 1118942085, 59239954, 837238868, 753246235, 1403394345, 886500603, 1648810182, 1540165060, 1680351736, 1044516203, 1655352860, 1381992751]

#answer = question01(portfolios)

#print answer
