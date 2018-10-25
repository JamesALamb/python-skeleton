# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#numnodes = 3
#edgelist = [{u'edgeA': 1, u'edgeB': 2}, {u'edgeA': 2, u'edgeB': 3}]
#numnodes = 5
#edgelist = [{u'edgeA': 1, u'edgeB': 2}, {u'edgeA': 1, u'edgeB': 3}, {u'edgeA': 1, u'edgeB': 4}, {u'edgeA': 1, u'edgeB': 5}]
numnodes = 5
edgelist = [{u'edgeA': 1, u'edgeB': 3}, {u'edgeA': 1, u'edgeB': 4}, {u'edgeA': 1, u'edgeB': 5}, {u'edgeA': 2, u'edgeB': 3}, {u'edgeA': 2, u'edgeB': 4}, {u'edgeA': 2, u'edgeB': 5}]

def question03(numNodes, edgeList):
  # modify and then return the variable below
  print numNodes, edgeList
#  edgeList = [ set(x.values()) for x in edgeList ]
  TrEx=set(range(1,numNodes+1))
  NotTrEx=set()
  
#  Count = [ [0] for i in range(numNodes) ]
#  for i in TrEx:
#    for j in edgelist:
#     if i in j:
#        Count[i-1][0] += 1
#  a = Count.index(max(Count))+1
#  TrEx.remove(a)
#  NotTrEx.add(a)
#  NewList = [x for x in edgeList if a not in x]

  NewList = edgeList

  while len(NewList) > 0:
    Count = [ [0] for i in range(numNodes) ]
    for i in TrEx:
      for j in NewList:
       if i in j.values():
          Count[i-1][0] += 1
    a = Count.index(max(Count))+1
    TrEx.remove(a)
    NotTrEx.add(a)
    NewList = [x for x in NewList if a not in x.values()]

  X = len(TrEx)
  Y = len(NotTrEx)

#  Y = 0
#  for i in NotTrEx:
#    for j in range(len(edgeList)):
#      if i in edgeList[j] and  edgeList[j].remove(i) < TrEx :
#        Y += 1
#        break
  
  answer = X-Y

  return answer

answer = question03(numnodes, edgelist)

print answer
