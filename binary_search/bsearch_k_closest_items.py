class Solution:
    #O(log(N-k)) + O(k) can be constant time too if arr.subarry(1,3) in java or 
    def findClosestElements(self, arr: List[int], k: int, x: int):
        # Initialize binary binary_search bounds
        left = 0
        right = len(arr) - k 
        
        # Binary binary_search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k] #left to left+k items



int search(int *array, int start_idx, int end_idx, int search_val) {

   if( start_idx == end_idx )
      return array[start_idx] <= search_val ? start_idx : -1;

   int mid_idx = start_idx + (end_idx - start_idx) / 2;

   if( search_val < array[mid_idx] )
      return search( array, start_idx, mid_idx, search_val );

   int ret = search( array, mid_idx+1, end_idx, search_val );
   return ret == -1 ? mid_idx : ret;
}
    