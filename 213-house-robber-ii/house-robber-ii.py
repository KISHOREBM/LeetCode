class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp1=[0]*(n-1)
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            dp1[i]=max(nums[i]+dp1[i-2],dp1[i-1])
        dp2=[0]*(n-1)
        dp2[0]=nums[1]
        dp2[1]=max(nums[1],nums[2])
        for i in range(2,n-1):
            dp2[i]=max(nums[i+1]+dp2[i-2],dp2[i-1])
        print(dp1,dp2)
        return max(dp1[-1],dp2[-1])
        