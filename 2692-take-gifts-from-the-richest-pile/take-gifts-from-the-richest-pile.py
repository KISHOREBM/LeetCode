import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            large=max(gifts)
            gifts[gifts.index(large)]=int(math.sqrt(large))
        return sum(gifts)

        