class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
            
        one, two, total = 1, 1, 0

        for i in range(n - 1):
            total= two + one
            two = one
            one =  total

        return total