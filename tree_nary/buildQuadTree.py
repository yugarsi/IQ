
# Definition for a QuadTree node.
from typing import List
'''
i,j      midy  y
     1  1   2  3
midx 1  1   1  1 
     0  0   1  1 
x    0  0   1  1 

'''


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def getNode():
            return Node(None, False, None, None, None, None)

        #checks if all elements are same
        def allSame(i, j, x, y):  # i,j = starting coordinates, x,y = end coordinates
            first = grid[i][j]
            for k in range(i, x):
                for l in range(j, y):
                    if grid[k][l] != first:
                        return False

            return True

        def buildTree(i, j, x, y, node):

            if allSame(i, j, x, y):
                node.val = grid[i][j]
                node.isLeaf = True  # Entire grid is same or not

            else:  # split into sub-parts and recurse
                midx = (i + x) // 2
                midy = (j + y) // 2

                node.topLeft = buildTree(i, j, midx, midy, getNode())
                node.topRight = buildTree(i, midy, midx, y, getNode())
                node.bottomLeft = buildTree(midx, j, x, midy, getNode())
                node.bottomRight = buildTree(midx, midy, x, y, getNode())

            return node

        return buildTree(0, 0, len(grid), len(grid[0]), getNode())
