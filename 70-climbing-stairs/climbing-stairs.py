class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        n1, n2 = 1, 2
        for i in range(3, n + 1):
            res = n1 + n2
            n1 = n2
            n2 = res
        return res
 
        