class Solution(object):
    def retBin(self,a):
        ret=0
        i=0
        while i<len(a):
            ret+=(int(a[len(a)-i-1])*2**i)
            i+=1
        return ret
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bi=self.retBin(a)+self.retBin(b)
        ret=0
        i=0
        while bi>0:
            rem=bi%2
            ret+=(rem*10**i)
            bi//=2
            i+=1
        return str(ret)

        