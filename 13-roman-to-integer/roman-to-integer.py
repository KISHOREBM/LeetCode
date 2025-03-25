class Solution(object):
    def romanToInt(self, s):
        dist={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        count=0
        for i in range(len(s)-1):
            if dist[s[i]]>=dist[s[i+1]]:
                count+=dist[s[i]]
            else:
                count-=dist[s[i]]
        return count+dist[s[-1]]

        