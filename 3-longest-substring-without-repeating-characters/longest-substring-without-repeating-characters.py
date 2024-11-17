class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        for i in range(len(s)):
            le=[]
            for j in s[i:]:
                if j in le:
                    break
                le.append(j)
            if len(le)>ret:
                ret=len(le)
        return ret
        