class Solution(object):
    def findClosestNumber(self, nums):
        mi=nums[0]
        for i in nums[1:]:
            if abs(i)<=abs(mi):
                if abs(i)==abs(mi):
                    mi=max(i,mi)
                else:
                    mi=i
        return mi
        