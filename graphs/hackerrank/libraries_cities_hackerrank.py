# for each connected component if cost of library is less, just build one lib and build roads
#for remaining cities.
# if cost_lib < cost_road then build library in every city
#Uses global variables to count number of nodes in each connected component of the graph
#cities are indexed 1 -> n

node_count = 0
def dfs(graph, visited, i):
    global node_count
    node_count += 1
    visited[i-1] = 1
    for n in graph[i]:
        if visited[n-1] == 0:
            dfs(graph, visited, n)
    
def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = defaultdict(list)
    for road in cities:
        u,v = road[0],road[1]
        graph[u].append(v)
        graph[v].append(u)
    
    visited  = [0] * n
    cost = 0 
    global node_count
    for i in range(1, n+1):
        #this is inside each component
        if visited[i-1] == 0:
            node_count = 0
            dfs(graph, visited, i)
            cost = cost + c_lib. #atleast one library should be built in a connected_component
            if c_lib > c_road:
                cost += (node_count-1) * c_road
            else:
                cost += (node_count-1) * c_lib
                
    return cost