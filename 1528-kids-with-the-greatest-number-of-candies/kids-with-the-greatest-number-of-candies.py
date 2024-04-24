class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest = max(candies)
        res = []

        for kid in candies:
            if kid + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)

        return res

        