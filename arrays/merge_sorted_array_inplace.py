class Solution:
    #nums1 has extra space and we need to merge 2 in 1
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #descending
        #[7,10,11,0,0,0 ]  [3,5,8] 
        
        i = m-1 #first array
        j = n-1 #second array
        k = len(nums1)-1 #add in first
        
        while i>=0 and j>=0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        
        while j>=0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
        
        while i>=0:
            nums1[k] = nums1[i]
            k-=1
            i-=1