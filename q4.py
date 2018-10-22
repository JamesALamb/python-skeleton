# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

X = 'X'
#rows, numberMachines = [[12, 12, 3, X, 3], [23, X, X, X, 3], [33, 21, X, X, X], [9, 12, 3, X, X], [X, X, X, 4, 5]] , 3
#rows, numberMachines = [[X, X, 2], [2, 3, X], [X, 3, 2]], 3
#rows, numberMachines = [[2, 3, X, 2], [4, X, X, 4], [3, 2, X, X], [X, X, X, 5]], 2 

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  totals = []
  for row in rows:
    numberX = row.count('X')
    c = 0
    values = []
    if ( numberX + numberMachines <= len(row) ):
      for i in row:
        if i != 'X':
          values.insert(0, int(i))
          c+=1
          if c >= numberMachines:
            total=0
            for j in range(numberMachines):
              total += values[j]
            totals.append(total)
        if i == 'X':
          c = 0
          values = []

  if totals == []:
    answer = 0
  else:
    answer = min(totals)

  return answer

#a = question04(rows, numberMachines)

#print a

