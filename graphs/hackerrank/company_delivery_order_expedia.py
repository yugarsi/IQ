'''
Delivery Management System A manufacturing company is located in a certain city.
Their goods need to be shipped to other cities that are connected with bidirectional roads, though some cities may not be accessible because roads don't connect to them.
The order of deliveries is determined first by distance, then by priority.
 Given the number of cities, their connections via roads, and that city the manufacturing company is located in determine the Order of cities where the goods will be delivered.
 For example, let's say that the number of cities is cityNodes - 4, where cityFrom = [1, 2, 2),
 cityTo = [2, 3, 4), and company - 1. In other words, the manufacturing company is located in city 1,
 and the roads run between cities 1 and 2, cities 2 and 3, and cities 2 and 4,
 like so: 3 1 in this case, the cities would be visited based on the following loge: The closest city (or cities) is visited first.
 This is city 2. which is 1 unit from the manufacturing company. The next-closest city for cities) is visited next.
 This is city 3 and city 4. which are both 2 units from the manufacturing company, in this case, priority is then calculated,
 visiting the smaller numbered oty first (aty 3) and continuing in ascending order (City 4).

'''
from collections import defaultdict

def getOrder(nodes, fromNodes, ToNodes, company):
    G = defaultdict(list)
    for i in range(1, nodes+1):
        G[i] = []

    for i in range(len(fromNodes)):
        G[fromNodes[i]].append(ToNodes[i])
        G[ToNodes[i]].append(fromNodes[i])

    for nodes in G:
        G[nodes] = G[nodes].sort()

    queue = [company]
    res = []
    visited = set()
    while queue:
        curr = queue.pop(0)
        visited.add(curr)
        res.append(curr)
        children = G[curr]
        for child in children:
            if child not in visited:
                queue.append(child)

    return res



