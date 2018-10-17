# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

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

def max(portfolios):
  # find max merged portfoli from matrix
  mat = matrix(portfolios)
  value = np.max(mat)
  index = np.where(mat == value) 
  print value
  print index
  return value, index

def binary(decimal):
  # get binary list from deciamal value
  binary = np.zeros((16,), dtype=int)
  for i in range(15,-1,-1):
    if (decimal - 2**i >= 0):
      decimal -= 2**i
      binary[15-i] = 1
  return binary

# TEST
a = 5000
b = binary(a)
print b

def decimal(binary):
  # get decimal value from binary list
  decimal = 0
  for i in range(16):
    decimal += binary[i] * 2**(15-i)
  return decimal

# TEST
c = decimal(b)
print c

def merge(value1, value2):
  # find value of merged portfolios
#  print value1
#  print value2
  a = binary(value1)
  b = binary(value2)
#  print a
#  print b
  c = np.add(binary(value1), binary(value2))
#  print c
  for i in range(len(c)):
    c[i] %= 2
#  print c
  value = decimal(c)
#  print value
  return value

def matrix(portfolios):
  #create matrix with largest merged values
  mat = np.zeros((len(portfolios), len(portfolios),), dtype=int)
  for i in range(len(portfolios)):
    for j in range(i+1, len(portfolios)):
      #if ( (portfolios[i] >= 2**15 and portfolios[j] < 2**15) or (portfolios[j] >= 2**15 and portfolios[i] < 2**15) ):
      mat[i, j] = merge(portfolios[i], portfolios[j])
  return mat
 
portfolios = np.random.randint(65535, size=int(sys.argv[1]))
#portfolios = np.array([31318, 60888, 13074, 22511, 55982, 17233, 44421, 47235, 48325, 9176])

#print portfolios

answer = question01(portfolios)

print answer

value, index = max(portfolios)

print "the max merged portfolio has a value of:", value, "and is created by the merging of portfolio", index[0][0] + 1, "and portfolio", index[1][0] + 1




