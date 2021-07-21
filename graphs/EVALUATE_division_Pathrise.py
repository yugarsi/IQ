'''
Evaluate division
equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]


Algorithm a/b = 2 , b/c = 3  ==> a/c == a/b * b/c = 2*3 = 6
So a -> b = 2 and b -> a will be edge of length
'''

from collections import defaultdict
#list of variables
def calcEquation(equations, values, queries):
    #Graph is a default  dict of dictionary as
    Graph = defaultdict(dict) #when there is edge weight graph adj list can be like this

    for i in range(len(equations)): #values and equations of same length
        first , second = equations[i][0], equations[i][1]
        v = values[i]
        Graph[first][second] = v
        Graph[second][first] = 1/v

    # BFS using q while not empty can also be a for loop
    def BFS(start, dest, graph):
        if not (start in graph) or not (dest in graph):
            return -1
        queue = [(start,1.0)]
        visited = set()

        for x, v in queue:
            if x == dest:
                return v
            visited.add(x)
            for y in Graph[x]:
                if y not in visited:
                    queue.append((y , v * graph[x][y]))
        return -1

    for start , dest in queries:
        print (BFS(start, dest, Graph))



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["a","x"]]

calcEquation(equations, values, queries)



