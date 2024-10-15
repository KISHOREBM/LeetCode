class Solution(object):
    def twoSum(self, nums, target):
        for i,v in enumerate(nums):
            for j in range(i+1,len(nums)):
                if v+nums[j]==target:
                    return [i,j]
        