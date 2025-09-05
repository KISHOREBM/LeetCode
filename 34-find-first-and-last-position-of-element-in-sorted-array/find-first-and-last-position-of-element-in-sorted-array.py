class Solution(object):
    def searchRange(self, nums, target):
        l,r=-1,-1
        for j,i in enumerate(nums):
            if i==target:
                if l==-1:
                    l=j
                r=j
        return [l,r]

        