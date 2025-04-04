import numpy as np
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        ret=max(piles)
        low=1
        right=max(piles)
        while low<=right:
            count=0
            mid=(low+right)//2
            for i in piles:
                if i<=mid:
                    count+=1
                else:
                    count+=np.ceil(i/float(mid))
                    # print(np.ceil(i/mid),i,mid)
            # print(count,mid)
            # print(ret,mid,count)
            if ret>mid and count<=h:
                ret=mid
            if count>h:
                low=mid+1
            else:
                right=mid-1
        return ret