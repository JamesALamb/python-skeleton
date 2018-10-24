# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
#import timeit

#compute all combinations for two portfolios
def question02(cashFlowIn, cashFlowOut):
  #print cashFlowIn, cashFlowOut
  # modify and then return the variable below
  I = np.array(cashFlowIn)
  O = - np.array(cashFlowOut)
  combined = np.append(I,O)
  A = sum(cashFlowIn)
  B = sum(cashFlowOut)
  mat = np.full((len(combined)+1, A+B+1), False, dtype=bool)
  for i in range(1,len(mat)):
    for j in range(len(mat[0])):
      if (combined[i-1] == j-B):
        mat[i,j] = True
        if j == B:

          answer = 0
          return answer

      if mat[i-1,j]:
        mat[i,j] = True
        if j == B:

          answer = 0
          return answer

      if ( j-combined[i-1] >= 0 ) and ( j-combined[i-1] < len(mat[0]) ):
        if mat[i-1,j-combined[i-1]]:
          mat[i,j] = True
          if j == B:

            answer = 0
            return answer

  answer = mat[len(combined),B:B+min(cashFlowIn)+1].tolist().index(True)

  #i = 0
  #index = []
  #subset = []
  #while 1 not in index:
    #ind = mat[:,B+answer-i].tolist().index(True)
    #index.append(ind)
    #subset.append(combined[ind-1])
    #i += combined[ind-1]

  #print index, subset, sum(subset)

  return answer

#cashFlowIn, cashFlowOut = [79, 954, 372, 842, 982, 562, 740], [513, 398, 535, 223, 693, 206, 922, 877, 486]

#start = timeit.default_timer()

#answer = question02(cashFlowIn, cashFlowOut)

#stop = timeit.default_timer()

#print answer
#print('Time: ', stop - start)
