# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  if totalValue <=0:

    answer = 0

    return answer

  allowedAllocations.sort(reverse=True)
  if sum(allowedAllocations) >= totalValue:
    count = 1
    while sum(allowedAllocations[:count]) < totalValue:
      count +=1

    answer = count

    return answer

  else:

    answer = 0

    return answer