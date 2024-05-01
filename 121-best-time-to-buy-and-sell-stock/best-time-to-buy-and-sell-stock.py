class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = prices[0]
        maxProfit = 0

        for p in prices:
            if p < buy:
                buy = p
            else:
                maxProfit = max(maxProfit, p - buy)
       
        return maxProfit


        