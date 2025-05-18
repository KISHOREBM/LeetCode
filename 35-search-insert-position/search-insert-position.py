class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        if nums[0]>=target:
            return 0
        while low<=high:
            mid=(low+high)//2
            print(mid)
            if nums[mid-1]<target and nums[mid]>=target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return len(nums)
        
        