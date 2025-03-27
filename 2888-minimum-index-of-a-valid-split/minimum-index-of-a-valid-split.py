from collections import Counter
class Solution(object):
    def minimumIndex(self, nums):
        value,count=Counter(nums).most_common(1)[0]
        prec=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]==value:
                prec+=1
                count-=1
                if (i+1-prec)<prec and (n-i-1-count)<count :
                    return i
                # print(i+1-prec,(len(nums)-i-1)-count,prec,count)
        return -1



        