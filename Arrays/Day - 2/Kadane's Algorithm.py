class Solution:
    def maxSubArray(self, nums):
        maxV = nums[0]
        sumV = 0
        for i in range(len(nums)):
            sumV += nums[i]
            maxV = max(maxV,sumV)
            if sumV <0:
                sumV = 0

        return maxV       
