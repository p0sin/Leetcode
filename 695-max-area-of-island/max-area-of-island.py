class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxIsland = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            # Explore adjacent unvisited land cells (using DFS recursively)
            pieceOfLand = 1
            pieceOfLand += dfs(row + 1, col)
            pieceOfLand += dfs(row - 1, col)
            pieceOfLand += dfs(row, col + 1)
            pieceOfLand += dfs(row, col - 1)

            return pieceOfLand

        for row in range(ROWS):
            for col in range(COLS):
                curIsland = dfs(row, col)
                maxIsland = max(maxIsland, curIsland)

        return maxIsland

        