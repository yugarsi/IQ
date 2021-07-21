class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        indegree = []
        for i in range(numCourses):
            indegree.append(0)
            graph[i] = set()
        

        for cr in prerequisites:
            first = cr[1] #first to take bi in order to take ai in [ai, bi]
            second = cr[0]
            graph[first].add(second)
            indegree[second] += 1
        
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        output = []
        while len(queue) != 0:
            curr = queue.pop(0)
            output.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(output) != numCourses:
            return []
        
        return output