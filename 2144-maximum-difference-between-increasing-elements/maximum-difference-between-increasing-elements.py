class Solution(object):
    def maximumDifference(self, nums):
        ma=0
        for i in range(len(nums)-1):
            ma=max(ma,max(nums[i+1:])-nums[i])
        return ma if ma!=0 else -1
        