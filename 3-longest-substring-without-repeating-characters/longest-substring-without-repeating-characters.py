class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        ret=0
        for i in range(len(s)):
            le=[]
            for j in s[i:]:
                if j in le:
                    break
                le.append(j)
            ret=max(ret,len(le))
        return ret
        