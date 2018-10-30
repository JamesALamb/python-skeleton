# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  I = np.array(cashFlowIn)
  O = - np.array(cashFlowOut)
  combined = np.append(O,I)
  if 0 in combined:

    return 0

  A = sum(cashFlowOut)
  B = min(cashFlowIn)
  mat = np.full((len(combined)+1, A+B+1), False, dtype=bool)
  for i in range(1,len(mat)):
    for j in range(len(mat[0])):
      if (combined[i-1] == j-A):
        mat[i,j] = True

      if mat[i-1,j]:
        mat[i,j] = True

      if ( j-combined[i-1] >= 0 ) and ( j-combined[i-1] < len(mat[0]) ):
        if mat[i-1,j-combined[i-1]]:
          mat[i,j] = True
          if j == A:

            return 0

  return mat[len(combined),A:].tolist().index(True)