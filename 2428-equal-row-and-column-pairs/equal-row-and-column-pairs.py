class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowCounts = defaultdict(int)

        res = 0

        for row in grid:
            rowCounts[tuple(row)] += 1

        for column in zip(*grid):
            res += rowCounts[column]

        return res