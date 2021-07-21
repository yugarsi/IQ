class Solution(object):
    
    #O(NlogN) for sort
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #we have to find overlapping intervals
        #sort both start times and end times
        
        starts = sorted(x[0] for x in intervals) #intervals sorted on just start time
        ends = sorted(x[1] for x in intervals) #entervals sorted based on end time


        rooms = 0

        #we have to find maximum overlapping meetings = maximum number of rooms
        j = 0 #j for ends and i is used for starts
        for i in range (len(starts)):
            rooms += 1  #keep adding rooms
            if starts[i] >= ends[j]: #if one has ended then empty rooms and update j
                rooms -= 1
                j +=1
                
        
        return rooms