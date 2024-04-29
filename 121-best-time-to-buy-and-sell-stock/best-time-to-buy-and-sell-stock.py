class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = prices[0]
        sell = 0
        maxProfit = 0

        for p in prices:
            if p < buy:
                maxProfit = max(maxProfit, sell - buy)
                sell = 0
                buy = p
            elif p > sell:
                sell = p
            
        maxProfit= max(maxProfit, sell-buy)

        return maxProfit


        