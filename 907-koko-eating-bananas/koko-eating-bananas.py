# import numpy as np
class Solution(object):
    def minEatingSpeed(self, piles, h):
        ret=max(piles)
        low=1
        right=ret
        while low<=right:
            count=0
            mid=(low+right)//2
            for i in piles:
                if i<=mid:
                    count+=1
                else:
                    count+=(i+mid-1)//mid
            if ret>mid and count<=h:
                ret=mid
            if count>h:
                low=mid+1
            else:
                right=mid-1
        return ret