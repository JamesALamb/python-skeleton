# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#allowedAllocations, totalValue = [1, 3, 4], 6
#allowedAllocations, totalValue = [3, 4], 6

def question05(allowedAllocations, totalValue):
  print allowedAllocations, totalValue
  # modify and then return the variable below
  if sum(allowedAllocations) > totalValue:
    allowedAllocations.sort(reverse=True)
    count = 0
    value = 0
    for i in range(len(allowedAllocations)):
      value += allowedAllocations[i]
      count +=1
      if value >= totalValue:
        break

    answer = count

    return answer

  else:

    answer = 0

    return answer

#answer = question05(allowedAllocations, totalValue)

#print answer
