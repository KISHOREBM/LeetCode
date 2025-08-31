class Solution(object):
    def canJump(self, nums):
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        m=nums[0]
        for i in nums[1:len(nums)-1]:
            m=max(i,m-1)
            if m<=0:
                # print(i,m)
                return False
        return True
        