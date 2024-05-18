class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def isValid(k, piles, h):
            totalHours = 0
            for p in piles:
                totalHours += (p + k - 1) // k  # Equivalent to math.ceil(p / k)
            return totalHours <= h

        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid, piles, h):
                r = mid - 1
            else:
                l = mid + 1
        
        return l


                