class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        path = [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, path):
        """
        backtracking method to check that no cycle would be formed starting from currCourse
        """
        if path[currCourse]:
            # come across a previously visited node, i.e. detect the cycle
            return True

        # before backtracking, mark the node in the path
        path[currCourse] = True

        # backtracking
        ret = False
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, path)
            if ret: break

        # after backtracking, remove the node from the path
        path[currCourse] = False
        return ret



class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses

        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, checked, path):
        """   """
        # 1). bottom-cases
        if checked[currCourse]:
            # this node has been checked, no cycle would be formed with this node.
            return False
        if path[currCourse]:
            # came across a marked node in the path, cyclic !
            return True

        # 2). postorder DFS on the children nodes
        # mark the node in the path
        path[currCourse] = True

        ret = False
        # postorder DFS, to visit all its children first.
        for child in courseDict[currCourse]:
            ret = self.isCyclic(child, courseDict, checked, path)
            if ret: break

        # 3). after the visits of children, we come back to process the node itself
        # remove the node from the path
        path[currCourse] = False

        # Now that we've visited the nodes in the downstream,
        #   we complete the check of this node.
        checked[currCourse] = True
        return ret