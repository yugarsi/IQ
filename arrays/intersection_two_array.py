class Solution(object):
    def intersection(self, nums1, nums2):
        res = set()
        hmap = collections.Counter(nums1)
        for i in nums2:
            if i in hmap and hmap[i] > 0:
                res.add(i)
                hmap[i] -= 1
        
        return list(res)