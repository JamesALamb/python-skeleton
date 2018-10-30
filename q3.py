# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  if edgeList == []:

    return numNodes

  TrEx=set(range(1,numNodes+1))
  NotTrEx=set()
  
  NewList = edgeList

  while len(NewList) > 0:
    Count = [ 0 for i in range(numNodes) ]
    for i in TrEx:
      for j in NewList:
       if i in j.values():
          Count[i-1] += 1
    a = Count.index(max(Count))+1
    TrEx.remove(a)
    NotTrEx.add(a)
    NewList = [x for x in NewList if a not in x.values()]

  X = len(TrEx)
  Y = len(NotTrEx)

  if X > Y:

    return X-Y

  else:

    return 0