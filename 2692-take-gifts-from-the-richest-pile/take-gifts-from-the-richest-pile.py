import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            large=math.sqrt(max(gifts))
            gifts[gifts.index(max(gifts))]=int(large)
        return sum(gifts)

        