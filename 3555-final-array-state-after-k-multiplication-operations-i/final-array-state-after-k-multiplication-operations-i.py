class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            mini=0
            for j in range(1,len(nums)):
                if nums[j] < nums[mini]:
                    mini=j
            nums[mini]=nums[mini]*multiplier
        return nums
        