class Solution(object):
    def longestNiceSubarray(self, nums):
        count=1

        for i in range(len(nums)):
            ma=1
            j=i+1
            used=nums[i]
            while j<len(nums) and used&nums[j]==0:
                ma+=1
                used|=nums[j]
                j+=1
            if ma>count:
                count=ma
        return count

        