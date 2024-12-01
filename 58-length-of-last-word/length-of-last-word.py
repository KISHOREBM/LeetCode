class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        i=len(s)-1
        got=0
        while i>=0:
            if s[i]!=" ":
                got=1
                ret+=1
            if s[i]==" " and got:
                return ret
            i-=1
        return ret



        