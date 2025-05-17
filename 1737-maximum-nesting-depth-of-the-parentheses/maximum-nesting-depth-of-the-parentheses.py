class Solution(object):
    def maxDepth(self, s):
        count=0
        m=0
        for i in s:
            if i=="(":
                count+=1
            elif i==")":
                m=max(count,m)
                count-=1
        return m
        