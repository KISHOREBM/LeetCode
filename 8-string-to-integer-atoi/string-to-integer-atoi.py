# def stdec(va):
#     if va=="" or not va[0].isdecimal():
#         return 0
#     return int(va[0])+10*stdec(va[1:])
class Solution(object):
    def myAtoi(self, s):
        mi=1
        start=0
        s=s.lstrip()
        if not s:
            return 0
        
        if s[start]=='-':
            mi=-1
            start+=1
        elif start<len(s) and s[start]=='+':
            start+=1
        val=0
        while start<len(s) and s[start].isdecimal():
            val=val*10+int(s[start])
            start+=1
        val=val*mi
        if val < -2147483648:
            return -2147483648
        if val > 2147483647:
            return 2147483647
        return val
        
        
        