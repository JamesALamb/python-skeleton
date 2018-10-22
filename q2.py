# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
#import sys

#cashFlowIn = np.random.randint(100, size=int(sys.argv[1]))
#cashFlowOut = np.random.randint(100, size=int(sys.argv[2]))

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  I = np.array(cashFlowIn)
  O = - np.array(cashFlowOut)
  combined = np.append(I,O)
  A = max(cashFlowIn)
  B = max(cashFlowOut)
  small = min(cashFlowIn)
  mat = np.full((len(combined), A+B+1), False, dtype=bool)
  for i in range(1,len(mat)):
    for j in range(len(mat[0])):
      if (combined[i-1] == j):
        mat[i,j] = True
      if mat[i-1,j]:
        mat[i,j] = True
      if mat[i-1,j-combined[i-1]]:
        mat[i,j] = True
  for i in range(small):
    if True in mat[:,B+i]:

      answer = i

      break

  return answer

#answer = question02(cashFlowIn, cashFlowOut)
