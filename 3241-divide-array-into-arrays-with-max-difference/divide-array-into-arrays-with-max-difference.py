class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        ret=[]
        left=0
        right=2
        while(right<len(nums)):
            if nums[right]-nums[left]<=k:
                ret.append(nums[left:right+1])
                left+=3
                right+=3
            else:
                return []
        return ret
        