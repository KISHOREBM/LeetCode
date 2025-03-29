class Solution(object):
    def calPoints(self, operations):
        val=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                val.append(int(i))
            elif i=='C':
                val.pop()
            elif i=='D':
                val.append(val[-1]*2)
            elif i=='+':
                val.append(val[-1]+val[-2])
        # print(val)
        s=0
        for i in val:
            s+=i
        return s
        