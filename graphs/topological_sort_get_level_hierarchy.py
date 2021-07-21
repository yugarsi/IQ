from collections import defaultdict

"""
[1,0],[3,2]

[[1,0],[2,0],[3,1],[3,2]]
n = 4

Output: [0,2,1,3]
"""
'''
0: 1, 2
1: 3
2: 3

1 <- 0
2 <- 0
3 <- 1
3 <- 2
'''
#using BFS
def getHierarchy(levels, num): #number of vertics
  graph = defaultdict(list)
  indegree = [0] * num
  for i in levels:
    first = i[0]
    second = i[1]
    if second in graph:
      graph[second] += [first] #append to existing list
    else:
      graph[second] = [first] #init adjacency list
    indegree[first] += 1
  
  queue = []
  for i in indegree:
    if indegree[i] == 0:
        queue.append(i)
  
  res = []
  while queue != []:
    node = queue.pop(0) #remove from top
    res.append(node)
    for neighbour in graph[node]:
        indegree[neighbour] -= 1
        if indegree[neighbour] == 0:
            queue.append(neighbour) #add to end
  return res


a = [[1,0],[2,0],[3,1],[3,2],[1,2]]
print(getHierarchy(a, 4))