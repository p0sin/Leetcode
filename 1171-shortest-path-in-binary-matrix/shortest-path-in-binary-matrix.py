class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
    
        N = len(grid)
        
        # Keep track of visited cells to avoid revisiting
        visited = set()
        
        # Use a queue for BFS exploration
        q = deque([(0, 0)])  # Start from top-left corner
        visited.add((0, 0))
        
        # Distance (number of steps) traveled so far
        distance = 1
        
        # Explore neighbors in all 8 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while q:
            # Process all elements in the current level
            for i in range(len(q)):
                r, c = q.popleft()

                if r == N - 1 and c == N - 1:
                    return distance

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if 0 <= new_r < N and 0 <= new_c < N and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
            # Increment distance after processing all nodes at the current level
            distance += 1

        return -1