class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        num1, num2 = 0, 1

        for i in range(2, n + 1):
            res = num1 + num2
            num1 = num2
            num2 = res
        return res