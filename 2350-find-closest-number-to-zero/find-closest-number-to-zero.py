class Solution(object):
    def findClosestNumber(self, nums):
        mi=nums[0]
        for i in nums[1:]:
            if abs(i)<=abs(mi):
                mi=min(abs(i),abs(mi))
        if abs(mi) in nums:
            return abs(mi)
        else:
            return abs(mi)*-1
        