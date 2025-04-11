class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for i in range(low,high+1):
            v=str(i)
            if len(v)%2==0:
                n=len(v)//2
                value=[int(char) for char in v]
                left=value[:n]
                right=value[n:]
                if sum(left)==sum(right):
                    count+=1
        return count
        