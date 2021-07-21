class Solution:
    #O(E+V) time complexity DFS ||| space = O(V) for visited O(E) for adj list => Total = O(E+V) 
    def countComponents(self, n, edges):
        graph = collections.defaultdict(list)

        for edge in edges:
            u,v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
            #undirected graph so we have to add edges like this both u->v and v->u
        
        visited = [0] * n
        
        #dfs algo
        def dfs(graph, start):
            visited[start] = 1
            for n in graph[start]:
                if visited[n] == 0:
                    dfs(graph, n)   
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count+=1
                dfs(graph, i)
        
        return count