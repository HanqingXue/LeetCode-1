class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        # initialise dp subarray
        dp = [0]*len(nums)
        # intialise base case for DP, first in array is best
        dp[0] = nums[0]
        
        # DP/Compare step
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
