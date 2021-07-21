class Solution(object):
    '''
    Find minimum number of knight moves to reach a destination x,y
    Trick is move in all possible directions 8 directions using BFS
    keep track of all visited while you iterate
    '''
    def minKnightMoves(self, x, y):

        """
        :type x: int
        :type y: int
        :rtype: int
        """
        target = (x, y)
        start = (0, 0)

        if target == start:
            return 0

        queue = [(start)]
        visited = set()

        steps = 0
        while queue:

            levellen = len(queue)

            for i in range(levellen):
                (curx, cury) = queue.pop(0)
                if (curx, cury) == target:
                    return steps

                pos1 = (curx + 1, cury + 2)
                pos2 = (curx + 2, cury + 1)
                pos3 = (curx + 2, cury - 1)
                pos4 = (curx + 1, cury - 2)

                pos5 = (curx - 1, cury - 2)
                pos6 = (curx - 2, cury - 1)
                pos7 = (curx - 2, cury + 1)
                pos8 = (curx - 1, cury + 2)

                if pos1 not in visited:
                    visited.add(pos1)
                    queue.append((pos1))

                if pos2 not in visited:
                    visited.add(pos2)
                    queue.append((pos2))

                if pos3 not in visited:
                    visited.add(pos3)
                    queue.append((pos3))

                if pos4 not in visited:
                    visited.add(pos4)
                    queue.append((pos4))

                if pos5 not in visited:
                    visited.add(pos5)
                    queue.append((pos5))

                if pos6 not in visited:
                    visited.add(pos6)
                    queue.append((pos6))

                if pos7 not in visited:
                    visited.add(pos7)
                    queue.append((pos7))

                if pos8 not in visited:
                    visited.add(pos8)
                    queue.append((pos8))

            steps += 1