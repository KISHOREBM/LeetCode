import numpy as np
class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        n=len(nums)
        nums=np.array(nums)
        while count<n:
            min1=np.min(nums[count:])
            # print(np.argmin(nums[count:]))
            nums=np.delete(nums,np.argmin(nums[count:])+count)
            min2=np.min(nums[count:])
            # print(np.argmin(nums[count:]))
            nums=np.delete(nums,np.argmin(nums[count:])+count)
            # print(nums[count:],count)
            nums=np.insert(nums,count,min2)
            count+=1
            # print(nums,count)
            nums=np.insert(nums,count,min1)
            count+=1
            # print(nums,count)
        return list(nums)
        