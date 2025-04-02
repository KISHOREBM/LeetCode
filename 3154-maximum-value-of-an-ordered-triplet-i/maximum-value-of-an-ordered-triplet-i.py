class Solution(object):
    def maximumTripletValue(self, nums):
        mv=0
        ls=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>=nums[i]:
                    break
                if nums[i]-nums[j]>mv:
                    mv=nums[i]-nums[j]
                    for k in nums[j+1:]:
                        if mv*k>ls:
                            ls=mv*k
        return ls
        