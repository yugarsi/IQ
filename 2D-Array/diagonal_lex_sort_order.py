
#given a
import collections


def getDiagonal(arr):
    hmap = collections.defaultdict(list)
    R = len(arr)
    C = len(arr[0])
    for r in range(R):
        for c in range(C):
            hmap[c-r+R].append(arr[r][c])   #c-r represents every parallel diagonals

    print (hmap)
    res = sorted(hmap.items(), key = lambda x:x[1])
    print (res)
    print(sorted(hmap.items()))

    a = [[1,2]]


a = [["z", "b","c"],
     ["a", "b", "c"],
     ["a", "b", "c"]]

getDiagonal(a)