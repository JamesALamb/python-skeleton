# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  if totalValue <=0 or totalValue < min(allowedAllocations):

    return 0

  else:
    allowedAllocations = list(set(allowedAllocations))
    allowedAllocations.sort(reverse=True)
    allowedAllocations = [x for x in allowedAllocations if x != 0]
    if set(allowedAllocations) == set(range(1,51)):

      return totalValue/50 +1

    A = max(allowedAllocations)
    mat_new = np.full((totalValue+1), False, dtype=bool)
    for i in allowedAllocations:
      mat_new[i] = True
    mat_old = [x for x in mat_new]
    c=2
    for i in range(totalValue/min(allowedAllocations)):
      for j in range(totalValue+1):
        if j <= c*A:
          if mat_old[j]:
            for k in allowedAllocations:
              mat_new[j+k] = True
              if j+k == totalValue:

                return c

      mat_old = [x for x in mat_new]
      c += 1

  if not mat_old[totalValue]:

    return 0