class Solution(object):
    def isAnagram(self, s, t):
        se=set(s) if len(s)>len(t)  else set(t)
        for i in se:
            if s.count(i)!=t.count(i):
                return False
        return True
        