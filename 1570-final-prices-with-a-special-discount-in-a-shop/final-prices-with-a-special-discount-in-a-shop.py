class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    prices[i]-=prices[j]
                    break
        return prices
        