# The pivot index is the index where the sum of all the numbers 
# strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        l_sum = 0
        for i in range(len(nums)):
            if (l_sum == total - l_sum - nums[i]):
                return i
            l_sum = l_sum + nums[i]
        
        return -1