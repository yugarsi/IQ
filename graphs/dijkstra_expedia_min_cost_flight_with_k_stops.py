import heapq, collections
class Solution:
    # O(V+E)LogV time complexity and O(V+E) space
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        1. can get all paths to dest
        2. can filter paths > k stops
        3. can sort remaining paths by cost

        so can start with djikstra, and discard path if path is too long

        '''
        Graph = collections.defaultdict(dict)  # adjacency list with cost as value
        visited = collections.defaultdict(int)  # sets default to 0 for every key

        for fr, to, price in flights:
            Graph[fr][to] = price

        # init source with k+1 stops as you aren't travelling to src
        # and cost is 0
        queue = [(0, src, k + 1)]

        while queue:
            totalcost, current, stops = heapq.heappop(queue)
            if current == dst:  # destination found
                return totalcost

            if visited[current] < stops:  # go further only if visited[current]< stops
                visited[current] = stops
                for neighbor, cost in Graph[current].items():
                    heapq.heappush(queue, (totalcost + cost, neighbor, stops - 1))

        return -1
