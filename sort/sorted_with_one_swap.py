
#given an array check if the array can be sorted with atmost one swap

#1 3 4 9 7 10 #consecutive elements are out of order

# 1 10 5 7 2 11  #10 and 2 not consecutive are out of order

def checkIfSorted(arr):
    invCount = 0
    first = 0
    second = 0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            invCount += 1
            if first == 0:
                first = i  #first inversion
            else:
                second = i #second inversion

    if invCount > 2:  #if > 2 inversions ==> not possible
        return False

    elif invCount == 1: #swap first-1 and first
        arr[first-1], arr[first] = arr[first], arr[first-1]
    elif invCount == 2: #swap first-1 and second
        arr[first-1], arr[second] = arr[second],arr[first-1]

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False

    return True

arr = [1, 10, 5, 7, 2, 11]
print (checkIfSorted(arr))