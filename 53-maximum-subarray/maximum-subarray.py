class Solution(object):
    def maxSubArray(self, nums):
        dp=[]
        for i in nums:
            dp.append(i)
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
        return max(dp)
        