#Find shortest distance between two nodes of same color
#runs BFS between unvisited O(Number of nodes)
#Val represents the target color
def bfs(graph, visited, ids, val, i):  #ids here represent colors corresponding to each graph node

    queue = []
    visited[i-1] = 1
    queue.append((i,0))
    
    while queue:
        curr, dist = queue.pop(0)
        for n in graph[curr]:
            if visited[n-1] == 0:
                visited[n-1] = 1
                queue.append((n, dist+1))
                if ids[n-1] == val:
                    mincost = dist + 1
                    return mincost
    return float("inf")
    

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(list)
    
    #constructing the graph
    for i in range(len(graph_from)):
        graph[graph_from[i]].append(graph_to[i])
        graph[graph_to[i]].append(graph_from[i])
    
    
    visited = [0] * graph_nodes
    ans = float("inf")
    for i in range(1, graph_nodes):
        if ids[i-1] == val:
            mincost = bfs(graph, visited, ids, val, i)
            ans = min(ans, mincost)
    
    if ans == float("inf"):
        return -1
    else:
        return ans