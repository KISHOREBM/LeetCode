class Solution(object):
    def check(self, nums):
        for i in range(len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]):
                i+=1
                for j in range(len(nums)-1):
                    if nums[i%len(nums)]>nums[(i+1)%len(nums)]:
                        return False
                    i+=1
        return True

        