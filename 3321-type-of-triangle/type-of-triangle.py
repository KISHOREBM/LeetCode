class Solution(object):
    def triangleType(self, nums):
        val=len(set(nums))
        if nums[0]+nums[1]<=nums[2] or nums[2]+nums[1]<=nums[0] or nums[0]+nums[2]<=nums[1]:
            return 'none'
        if val==1:
            return 'equilateral'
        elif val==2:
            return 'isosceles'
        else:
            return 'scalene' 
        