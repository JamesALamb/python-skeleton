# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

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
    return 0
  else:
    return min(totals)