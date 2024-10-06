class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = sorted(nums1 + nums2)  
        n = len(merged_array)
        
       
        if n % 2 == 1: 
            median = merged_array[n // 2]
        else:  
            median = (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2.0
        
        return median


demo = Solution()
print(demo.findMedianSortedArrays([3, 4, 5], [76, 55, 55]))

        