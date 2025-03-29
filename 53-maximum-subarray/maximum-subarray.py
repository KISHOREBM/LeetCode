class Solution(object):
    def maxSubArray(self, nums):
        cu=nums[0]
        ma=nums[0]
        for i in nums[1:]:
            cu=max(cu,0)
            cu+=i
            ma=max(cu,ma)
            
        return ma
        