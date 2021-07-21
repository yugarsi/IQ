class Solution:
    #greedy solution is optimal and O(n^2)
    #brute force is graph and finding connected componenet
    #intervals given as list of list [[1,4] [5,6] [6,9]]
    def merge(self, intervals):
        intervals.sort()
        #can also use intervals.sort(key=lambda x: x[0])

        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        
    
        for i in intervals[1:]:
            if i[0] > end:
                res.append([start,end])
                start = i[0]
                end = i[1]
            elif i[0] <= end and i[1] > end:
                end = i[1]
            elif i[0] < end and i[1] <= end:
                continue
        
        res.append([start,end])
        
        return res
            