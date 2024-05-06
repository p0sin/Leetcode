class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # option 1        
        # cache = {}

        # if n in cache:
        #     return chache[n]
        # elif n < 2:
        #     cache[n] = n
        #     return cache[n]
        # else:
        #     cache[n] = self.fib(n - 1) + self.fib(n - 2)

        #     return cache[n]

        # option 2
        if n == 0:
            return 0
        elif n == 1:
            return 1

        one, two = 0, 1
        for num in range(2, n):
            temp = two
            two = one + two
            one = temp

        return one + two
    