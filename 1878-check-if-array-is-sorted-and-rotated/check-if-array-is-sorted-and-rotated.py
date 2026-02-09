class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
        for i in range(n-1):
            if nums[i]>nums[i+1] :
                    count+=1
        if nums[-1]>nums[0]:
            count+=1
        if count>1:
            return False
        return True
        