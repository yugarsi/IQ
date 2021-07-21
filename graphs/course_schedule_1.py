#given a lest of course and prereq return if student can finish all courses or not
#O(V+E) time and O(V+E) space
class Solution:
    #using topological sorting
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indirection = []
        
        for i in range(numCourses):
            graph[i] = []
            indirection.append(0)
            
        for course in prerequisites:
            first = course[0]
            second = course[1]
            graph[first].append(second)
            indirection[second] += 1
        
        queue = []
        for i in range(len(indirection)):
            if indirection[i] == 0:
                queue.append(i)
        
        removed_edges = 0
        while queue != []:
            curr = queue.pop(0)
            for n in graph[curr]:
                indirection[n] -= 1
                removed_edges += 1
                if indirection[n] == 0:
                    queue.append(n)
        
        total_depths = len(prerequisites) #this indicates all edges visited and there are no cycles
        if removed_edges == total_depths:
            return True
        else:
            return False