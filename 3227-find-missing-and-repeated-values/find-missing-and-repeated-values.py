from collections import Counter
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        a=[item for lis in grid for item in lis]
        missing=0
        for i in range(1,len(a)+1):
            if i not in a:
                missing=i
                break
        m=Counter(a).most_common()[0][0]
        return [m,missing]
        