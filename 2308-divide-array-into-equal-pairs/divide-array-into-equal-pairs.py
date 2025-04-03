class Solution(object):
    def divideArray(self, nums):
        se=set(nums)
        for i in se:
            if nums.count(i)%2!=0:
                return False
        return True
        