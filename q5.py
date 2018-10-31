# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  if totalValue <=0 or totalValue < min(allowedAllocations):

    return 0

  elif totalValue%max(allowedAllocations) == 0

    return totalValue/max(allowedAllocations)

  elif totalValue%max(allowedAllocations) in allowedAllocations:

    return totalValue/max(allowedAllocations) + 1

  else:
    allowedAllocations = list(set(allowedAllocations))
    allowedAllocations = [x for x in allowedAllocations if x != 0]
    A = max(allowedAllocations)
    B = min(allowedAllocations)
    C = totalValue/B
    lA = range(1,C+1) 
    lB = range(1,C+1)    
    lA = [min(A*x, totalValue) for x in lA]
    lB = [B*x for x in lB]

    mat_new = np.full((totalValue+1), False, dtype=bool)
    c=1
    for i in allowedAllocations:
      if i == totalValue:

        return c

      elif i < totalValue:
        mat_new[i] = True

    mat_old = [x for x in mat_new]

    for i in range(C):
      for j in range(lB[i],lA[i]+1):
        c += 1
        if mat_old[j]:
          for k in allowedAllocations:
            if j+k == totalValue:

              return c

            elif j+k < totalValue:
              mat_new[j+k] = True

        mat_old = [x for x in mat_new]


  if not mat_old[totalValue]:

    return 0