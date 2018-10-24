# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#cashflow_in = [66, 293, 215, 188, 147, 326, 449, 162, 46, 350]
#cashflow_out = [170, 153, 305, 290, 187]
#cashflow_in = [189, 28]
#cashflow_out = [43, 267, 112, 166]
#cashflow_in = [72, 24, 73, 4, 28, 56, 1, 43]
#cashflow_out = [27]

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  print cashFlowIn, cashFlowOut
  I = np.array(cashFlowIn)
  O = - np.array(cashFlowOut)
  combined = np.append(I,O)
  A = sum(cashFlowIn)
  B = sum(cashFlowOut)
  small = min(cashFlowIn)
  mat = np.full((len(combined)+1, A+B+1), False, dtype=bool)
#  print combined, mat.shape
  for i in range(1,len(mat)):
#    print np.count_nonzero(mat)
#    print mat[i-1,:]
    for j in range(len(mat[0])):
      if (combined[i-1] == j-B):
#        print i,j, combined[i-1], j-B
        mat[i,j] = True
#        print mat[:,j]
      if mat[i-1,j]:
#        print i, j
        mat[i,j] = True
#        print mat[:,j]
      if ( j-combined[i-1] >= 0 ) and ( j-combined[i-1] < len(mat[0]) ):
        if mat[i-1,j-combined[i-1]]:
#        print i, j, combined[i-1], j-combined[i-1]
          mat[i,j] = True
#        print mat[:,j]
  for i in range(small+1):
#    print B+i, mat[:,B+i]
    if mat[len(combined),B+i]:

      answer = i

      break
    else:

      answer = small

  return answer

#answer i= question02(cashflow_in, cashflow_out)

#print answer
