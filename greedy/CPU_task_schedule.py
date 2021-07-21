# '''
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. 
#Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# '''

class Solution:
    #input = ["A","A","A","B","B", "C"]
    #["A", , ,"A", , ,"A"] total+idle_time = (fmax -1 ) * time_of_rest

    #rest is how many units of rest
    def leastInterval(self, tasks, rest):
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1 #ord is ascii key of char a
        
        frequencies.sort()
        #least to most
        # max frequency
        f_max = frequencies.pop() #pop() pops out the last most frequent element
        idle_time = (f_max - 1) * rest
        
        #most of the remaining tasks can be accomodated in the gap 
        #as they are less frequent than the firt job
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        
        idle_time = max(0, idle_time)
        return idle_time + len(tasks) ##Remember!

    def leastInterval2(self, tasks, n):
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)