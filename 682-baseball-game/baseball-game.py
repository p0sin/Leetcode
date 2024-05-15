class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Initialize scores
        scores = []
        ans = 0
        # Iterate over each operation and perfom it
        for op in operations:
            if op == "C":
                ans -= scores[-1]
                scores.pop()

            elif op == "+":
                scores.append(scores[-1] + scores[-2])
                ans += scores[-1]
            elif op == "D":
                scores.append(scores[-1] * 2)
                ans += scores[-1]
            else:
                scores.append(int(op))
                ans += scores[-1]

        return ans
                

        