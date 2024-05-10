class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue

                left_path = up_path = float('inf')
                if i != 0:
                    up_path = grid[i][j] + grid[i-1][j]
                if j != 0:
                    left_path = grid[i][j] + grid[i][j-1]

                grid[i][j] = min(left_path, up_path)

        return grid[m-1][n-1]
        