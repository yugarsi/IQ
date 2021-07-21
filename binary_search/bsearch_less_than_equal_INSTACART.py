def bsearch (self, nums, start, end, target):
    if nums[end] <= target:
        return end

    while start + 1 < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid
        else:
            start = mid

    if nums[start] <= target:
        return start
    else:
        return -1