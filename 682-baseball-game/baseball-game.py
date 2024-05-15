class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Initialize scores
        scores = []
        # Iterate over each operation and perfom it
        for op in operations:
            if op == "C":
                scores.pop()
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(scores[-1] * 2)
            else:
                scores.append(int(op))

        return sum(scores)
                

        