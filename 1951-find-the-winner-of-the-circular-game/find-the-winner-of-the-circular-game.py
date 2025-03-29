class Solution(object):
    def findTheWinner(self, n, k):
        val=list(range(1,n+1))
        index=0
        while len(val)>1:
            index=(index+k-1)%len(val)
            val.pop(index)
        return val[0]