class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        
        cache = {}

        if n in cache:
            return chache[n]
        elif n < 2:
            cache[n] = n
            return cache[n]
        else:
            cache[n] = self.fib(n - 1) + self.fib(n - 2)

            return cache[n]
    