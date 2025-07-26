class Solution(object):
    def minAddToMakeValid(self, s):
        l=[]
        c=0
        for i in s:
            if i=='(' or len(l)<=0:
                l.append(i)
            elif i==')' and l[-1]=='(':
                l.pop() 
            else:
                c+=1
        return len(l)+c