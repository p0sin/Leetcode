class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[cols - 1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c + 1]
                

        return dp[0]
