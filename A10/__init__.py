#nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#
def get_all_subsets(arr):
    n = len(arr)
    res = [[]]
    for i in range(pow(2,n)):
        for j in range(0, len(arr)):
            if( i & (1 << j)) > 0:
                res.append(arr[j])



arr = [1,2,3]
print (get_all_subsets(arr))

