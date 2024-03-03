class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        num = sorted(num)
        l = len(num)
        median_index = (l//2)
        if l & 1:
            # num[median_index+1-1] -> 0 indexing
            median_value = num[median_index]
        else:
            # num[median_index-1]+num[median_index+1-1] -> 0 indexing
            median_value = (num[median_index-1]+num[median_index])/2
        return median_value
