# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
#import timeit

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  #print cashFlowIn, cashFlowOut
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

#  index = []
#  subset = []

#  ind = mat[:,B+answer-sum(subset)].tolist().index(True)
#  print subset, mat[:,B+answer-sum(subset)], ind, combined[ind-1], combined[ind]
#  index.append(ind)
#  subset.append(combined[ind-1])

#  while sum(subset) != answer:
#    ind = mat[:,B+answer-sum(subset)].tolist().index(True)
#    index.append(ind)
#    subset.append(combined[ind-1])

#  print index, subset, sum(subset)

  return answer

#cashflow_in = [66, 293, 215, 188, 147, 326, 449, 162, 46, 350]
#cashflow_out = [170, 153, 305, 290, 187]
#cashflow_in = [189, 28]
#cashflow_out = [43, 267, 112, 166]
#cashflow_in = [72, 24, 73, 4, 28, 56, 1, 43]
#cashflow_out = [27]

#cashflow_in, cashflow_out = [271, 374, 663, 884, 283, 116, 508, 285, 839], [822, 375, 389, 634, 491, 976, 251, 530, 998]

#start = timeit.default_timer()

#answer = question02(cashflow_in, cashflow_out)

#stop = timeit.default_timer()

#print answer
#print('Time: ', stop - start)
