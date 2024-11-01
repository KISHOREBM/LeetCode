class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=1
        ret=s[0]
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                count+=1
                if(count>=3):
                    continue
                ret+=s[i]
            else:
                count=1
                ret+=s[i]
        return ret
        