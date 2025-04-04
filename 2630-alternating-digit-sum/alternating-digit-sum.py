def find(n,lis):
    if n<=0:
        return 
    find(n/10,lis)
    lis.append(n%10)
class Solution(object):
    def alternateDigitSum(self, n):
        lis=[]
        find(n,lis)
        s=0
        for i in range(len(lis)):
            if i%2==0:
                s+=lis[i]
            else:
                s-=lis[i]
        return s
        