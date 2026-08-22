class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]
        else:
            mid = n // 2
            return (nums[mid - 1] + nums[mid]) / 2