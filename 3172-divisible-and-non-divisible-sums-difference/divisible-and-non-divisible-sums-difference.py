class Solution(object):
    def differenceOfSums(self, n, m):
        no=0
        y=0
        for i in range(1,n+1):
            if i%m==0:
                y+=i
            else:
                no+=i
        # print(no,y)
        return no-y
        