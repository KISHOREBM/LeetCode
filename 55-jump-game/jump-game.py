def nonNegative(nums,n):
    p=n
    while n>=0:
        print(p,n)
        if nums[n]!=0 and nums[n]>=(p-n+1):
            return p-n
        
        n=n-1
    return -1
class Solution(object):
    def canJump(self, nums):
        n=len(nums)-2
        while n>=0:
            if nums[n]==0 :
                val=nonNegative(nums,n)
                if val==-1:
                    return False
                else:
                    n=n-val
            n=n-1
        return True