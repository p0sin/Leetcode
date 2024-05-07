class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0 

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            dfs(r - 1, c) # Up
            dfs(r + 1, c) # Down
            dfs(r, c - 1) # Left
            dfs(r, c + 1) # Right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1': # Found Island
                    islands += 1
                    dfs(r, c) # Check for adjacent piece of land

        return islands