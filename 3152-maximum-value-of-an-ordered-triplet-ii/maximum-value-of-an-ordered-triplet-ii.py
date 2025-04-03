class Solution(object):
    def maximumTripletValue(self, nums):
        ma=0
        mi=0
        ret=0
        marr=[nums[-1]]
        for i in nums[-1::-1]:
            if i > marr[0]:
                marr.insert(0,i)
            else:
                marr.insert(0,marr[0])
        print(marr)
        for j,i in enumerate(nums):
            ret=max(ret,(ma-mi)*marr[j])
            if i>ma:
                ma=i
                mi=i
            if i<mi:
                mi=i
        return ret
