class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        mx = float("-inf")
        for i in range(len(nums)):
            if dp[i]>0:
                dp[i+1] = dp[i] + nums[i]
            else:
                dp[i+1] = nums[i]
            mx = max(mx, dp[i+1])
        return mx