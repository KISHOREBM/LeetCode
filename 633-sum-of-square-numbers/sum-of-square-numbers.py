import math
class Solution(object):
    def judgeSquareSum(self, c):
        if int(math.sqrt(c))**2==c:
            return True
        i=1
        num=c-(i*i)
        while num>0:
            if int(math.sqrt(num))**2==num:
                print(num,i)
                return True
            i+=1
            num=c-(i*i)
        return False
        