class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_island = 0  # Using snake_case for variable naming consistency

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0  # Mark cell as visited

            area = 1  # Initialize area for current island
            area += dfs(row + 1, col)  # Explore up
            area += dfs(row - 1, col)  # Explore down
            area += dfs(row, col + 1)  # Explore right
            area += dfs(row, col - 1)  # Explore left

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_island = max(max_island, dfs(row, col))  # Update max_island

        return max_island

        