class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        # n=n*n
        # while(n>0):
        #     if n*w <=maxWeight:
        #         return n
        #     n-=1
        # return 0
        return min(n*n,maxWeight/w)
        