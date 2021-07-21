'''
MajorityElement
'''

#boyer moore's voting algorithm

'''
select one element as majority element and increment count += 1 if same found next
and then for every other element encountered count -= 1
If count becomes 0 then init the next element as mojirity element.
this will always return a solution
'''
class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        majorityElement = None
        for i in range(len(nums)):
            if count == 0:
                majorityElement = nums[i]
            if nums[i] == majorityElement:
                count += 1
            else:
                count -= 1

        return majorityElement