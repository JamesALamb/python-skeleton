# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  # modify and then return the variable below
  I = np.array(cashFlowIn)
  O = - np.array(cashFlowOut)
  combined = np.append(O,I)
  if 0 in combined:

    answer = 0

    return answer

  A = sum(cashFlowIn)
  B = sum(cashFlowOut)
  mat = np.full((len(combined)+1, A+B+1), False, dtype=bool)
  for i in range(1,len(mat)):
    for j in range(len(mat[0])):
      if (combined[i-1] == j-B):
        mat[i,j] = True

      if mat[i-1,j]:
        mat[i,j] = True

      if ( j-combined[i-1] >= 0 ) and ( j-combined[i-1] < len(mat[0]) ):
        if mat[i-1,j-combined[i-1]]:
          mat[i,j] = True
          if j == B:

            answer = 0

            return answer

  answer = mat[len(combined),B:B+min(cashFlowIn)+1].tolist().index(True)

  return answer
