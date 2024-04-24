class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest = max(candies)
        res = [i + extraCandies >= greatest for i in candies]

        return res

        