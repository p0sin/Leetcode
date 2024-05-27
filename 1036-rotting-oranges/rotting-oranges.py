class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))

        minutes = 0
        while rotten:
            if not fresh:
                return minutes
            for _ in range(len(rotten)):

                r, c = rotten.popleft()

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]         
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if (new_r, new_c) in fresh:
                        rotten.append((new_r, new_c))
                        fresh.remove((new_r, new_c))
                        grid[new_r][new_c] == 2

            # Add 1 minutes once all adjacent fresh tomatoes are rotten   
            minutes += 1 
            
        if fresh:
            return -1
        else:
            return minutes

        



