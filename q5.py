# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question05(allowedAllocations, totalValue):
  # modify and then return the variable below
  print allowedAllocations, totalValue
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

#allowedAllocations, totalValue = [7, 8, 3, 36, 16, 31, 48, 15, 4, 0, 19, 38, 33, 11, 50, 15, 1, 34, 23, 10, 14, 28, 24, 21, 39, 34, 31, 40, 50, 33, 0, 48, 38, 26, 18, 12, 5, 13, 26, 32, 24, 36, 16, 43, 39, 7, 26, 43, 27, 26, 8, 44, 39, 41, 36, 12, 44, 18, 16, 17, 38, 1, 10, 15, 0, 14, 25, 35, 43, 31, 33, 13, 13, 7, 44, 13, 46, 13, 1, 37, 7, 3, 31, 7, 38, 50, 37, 18, 40, 19, 49, 25, 46, 18, 46, 40, 38, 27, 9, 41, 45, 44, 13, 49, 40, 29, 20, 45, 44, 29, 8, 29, 37, 13, 26, 44, 46, 17, 8, 22, 45, 40, 32, 30, 25, 14, 24, 7, 1, 19, 10, 25, 26, 18, 27, 41, 35, 35, 33, 26, 28, 41, 30, 42, 19, 38, 17, 41, 43, 39, 2, 12, 40, 38, 29, 26, 41, 41, 38, 6, 3, 41, 25, 34, 29, 16, 25, 20, 2, 40, 6, 5, 41, 35, 47, 47, 45, 39, 44, 12, 45, 14, 17, 5, 38, 16, 0, 13, 29, 48, 19, 38, 34, 13, 20, 21, 50, 47, 35, 9, 17, 10, 3, 23, 36, 38, 8, 35, 19, 37, 44, 34, 10, 19, 28, 31, 29, 6, 45, 12, 38, 33, 0, 15, 13, 6, 43, 36, 11, 15, 8, 41, 45, 0, 27, 8, 36, 7, 49, 6, 31, 25, 9, 41, 32, 34, 19, 45, 25, 35, 46, 25, 41, 14, 43, 13, 39, 10, 22, 33, 24, 45, 23, 18, 11, 29, 41, 8, 7, 40, 16, 33, 19, 18, 47, 49, 47, 9, 9, 40, 17, 13, 22, 30, 37, 29, 33, 1, 24, 7, 7, 41, 9, 20, 1, 0, 28, 14, 10, 8, 15, 3, 22, 3, 39, 16, 29, 0, 11, 27, 23, 2, 46, 29, 36, 1, 16, 20, 28, 8, 12, 19, 28, 31, 40, 19, 4, 17, 10, 17, 10, 43, 47, 45, 38, 11, 35, 14, 44, 17, 30, 37, 49, 33, 8, 0, 44, 0, 48, 48, 21, 23, 38, 45, 10, 2, 45, 32, 14, 20, 25, 25, 15, 17, 27, 10, 4, 7, 22, 6, 7, 13, 39, 2, 44, 45, 11, 11, 16, 6, 34, 14, 34, 4, 41, 47, 1, 13, 35, 42, 23, 19, 14, 16, 38, 42, 20, 15, 2, 28, 29, 15, 9, 17, 4, 8, 46, 49, 40, 31, 12, 49, 9, 32, 7, 47, 36, 22, 12, 3, 35, 4, 10, 50, 40, 29, 21, 27, 39, 16, 29, 6, 27, 43, 17, 22, 16, 38, 28, 26, 15, 10, 32, 45, 5, 36, 43, 1, 27, 44, 2, 6, 39, 34, 36, 48, 41, 49, 28, 23, 26, 7, 46, 14, 3, 4, 31, 13, 23, 20, 47, 3, 37, 0, 27, 4, 14, 14, 35, 49], 8939

#answer = question05(allowedAllocations, totalValue)

#print answer
