import numpy as np
class Solution(object):
    def maximumCandies(self, candies, k):
        if sum(candies)<k:
            return 0
        low=1
        ma=sum(candies)//k
        res=0
        while low<=ma:
            total=0
            mid=(ma+low)//2
            for i in candies:
                total+=i//mid
                if total>=k:
                    break
            if total>=k:
                res=mid
                low=mid+1
            else:
                ma=mid-1
        return res
            




        
           




        