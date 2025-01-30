class Solution(object):
    def myAtoi(self, s):
        flag=1
        visited=0
        fvisited=0
        ret=""
        for i in s:
            if i==' ' and visited+fvisited ==0:
                continue
            if i.isnumeric():
                visited=1
                ret=ret+i
            elif (i=='-' or i=='+') and visited+fvisited ==0:
                flag=int(i+'1')
                fvisited=1
            else:
                break
        if visited ==0:
            return 0
        ret=int(ret)*flag
        if ret <= -2147483648:
            return -2147483648
        elif ret >=2147483647:
            return 2147483647
        else:
            return ret
        
        
        