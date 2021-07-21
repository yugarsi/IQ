import collections
class Solution:
    '''
    Core - Algo
    Can be solved with topological sort if no cycles

    At each airport, given a list of possible destinations, while backtracking, at
    each step we would pick the destination greedily in lexical order,
    i.e. the one with the smallest lexical order would have its trial first.

    '''

    '''
    Hierholzer's Algorithm!!!!

    In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph 
    that visits every edge exactly once 

    (allowing for revisiting vertices).

    We can visit vertices multiple times but edges only once to find the entire     
    itinerary.
    It starts with a random node and then follows an arbitrary unvisited edge to a neighbor. 
    This step is repeated until one returns to the starting node. This yields a first circle in the graph.
    If this circle covers all nodes it is an Eulerian cycle and the algorithm is finished. 
    Otherwise, one chooses another node among the cycles' nodes with unvisited edges and constructs another circle, called subtour.
    '''


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        #O(Elog(E/V)) time and  O(E+V)space
        def DFS(origin):
            destList = self.Graph[origin]
            while destList:
                # while we visit the edge, we trim it off from graph.
                nextDest = destList.pop()
                DFS(nextDest)
            self.result.append(origin)

        self.Graph = collections.defaultdict(list)

        # sort the itinerary based on the lexical order
        # Note that we could have multiple identical flights,
        # i.e. same origin and destination.
        tickets.sort(key=lambda x: x[1], reverse=True)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.Graph[origin].append(dest)

        self.result = []
        DFS('JFK')

        # reconstruct the route backwards
        return reversed(self.result)
