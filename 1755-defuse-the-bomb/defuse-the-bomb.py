class Solution(object):
    @staticmethod
    def minus(code,n):
        i=0
        ret=[0]*len(code)
        while i<len(code):
            for j in range(n):
                ret[i]+=code[(len(code)-j-1+i)%len(code)]
            i+=1
        return ret
    @staticmethod
    def plusd(code,n):
        i=0
        ret=[0]*len(code)
        while i<len(code):
            for j in range(n):
                ret[i]+=code[(i+j+1)%len(code)]
            i+=1
        return ret
    def decrypt(self, code, k):
        i=0
        if k<0:
            n=k*-1
            return Solution.minus(code,n)
        elif k==0:
            return [0]*len(code)
        else:
            return Solution.plusd(code,k)
        
        