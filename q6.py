# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  fastest_times = times[0]
  visited = [0]
  visit = 0
  for i in range(numServers):
    for j in range(1,numServers):
      if visit in visited:
        visit = fastest_times.index(sorted(fastest_times)[j])
      else:
        break
    visited.append(visit)
    #update times
    new_times = times[visit]
    for j in range(numServers):
      if (new_times[j] + fastest_times[visit] < fastest_times[j]):
        fastest_times[j] = new_times[j] + fastest_times[visit]
    if (visit == targetServer):
      break

  answer = fastest_times[targetServer]

  return answer

