class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=1
        ret=s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
                if(count<3):
                    ret+=s[i]
            else:
                ret+=s[i]
                count=1
        return ret
        