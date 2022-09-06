# running sum of an array is defined as runningSum[i] = sum(nums[0]…nums[i]).

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output =[0]*len(nums)
        output[0] = nums[0]
        for i in range(1,len(nums)):
            output[i] = output[i-1] + nums[i]
        
        return output