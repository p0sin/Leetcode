class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            # Base cases to handle out-of-bounds or visited cells
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"  # Mark cell as visited to prevent revisiting

            # Explore adjacent unvisited land cells (using DFS recursively)
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Iterate through the grid, calling DFS for each unvisited "1" cell
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands
        

        
