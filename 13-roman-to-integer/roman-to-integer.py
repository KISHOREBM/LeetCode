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
        for a,b in zip(s,s[1:]):
            if dist[a] < dist[b]:
                count-=dist[a]
            else:
                count+=dist[a]
        return count+dist[s[-1]]

        