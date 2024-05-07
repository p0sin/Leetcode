class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # OPTION 1 RECURSIVE BACK TRACKING        
        # if n <= 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        # OPTION 2 TOP DOWN WITH MEMOIZATION
        # memo = {}
        # if n in memo:
        #     return memo[n]
        # elif n <= 1:
        #     return n
        # else:
        #     memo[n] = self.fib(n - 1) + self.fib(n - 2)

        # return memo[n]

        # OPTION 3 BOTTOM-UP WITH TABULATION
        # if n <= 1:
        #     return n
        # tab = [0, 1]

        # for i in range(2, n + 1):
        #     tab.append(tab[i - 1] + tab[i - 2])

        # return tab[n]

        # OPTION 4 BOTTOM-UP WITH NO MEMORY
        if n <= 1:
            return n

        a, b = 0, 1

        for i in range(2, n + 1):
            temp = b
            b += a
            a = temp

        return b