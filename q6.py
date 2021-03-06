# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  if targetServer == 0:

    return 0

  fastest_times = times[0]
  visited = [0]
  visit = 0
  for i in range(len(times[visit])):
    for j in range(1, len(times[visit])):
      if visit in visited:
        visit = times[visit].index(sorted(times[visit])[j])
      else:
        break
    visited.append(visit)
    new_times = times[visit]
    for j in range(len(times[visit])):
      if (new_times[j] + fastest_times[visit] < fastest_times[j]):
        fastest_times[j] = new_times[j] + fastest_times[visit]
    if (visit == targetServer):
      break

  return fastest_times[targetServer]