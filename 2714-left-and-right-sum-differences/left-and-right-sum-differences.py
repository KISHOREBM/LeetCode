class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightsum=[0]
        s=sum(nums[1:])
        count=0
        for i in nums[1:]:
            rightsum.insert(count,s)
            s=s-i
            count+=1
        s=0
        leftsum=[0]
        for i in nums[:-1]:
            s=s+i
            leftsum.append(s)
        return [abs(leftsum[i]-rightsum[i]) for i in range(len(leftsum)) ]

        