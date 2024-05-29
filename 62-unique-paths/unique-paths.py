class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the previous row with zeros
        prev_row = [0] * n

        # Iterate from the bottom row to the top row
        for r in range(m - 1, -1, -1):
            # Initialize the current row with zeros
            curr_row = [0] * n
            # Set the rightmost cell of the current row to 1
            curr_row[n - 1] = 1
            # Iterate from the second rightmost cell to the leftmost cell
            for c in range(n - 2, -1, -1):
                # Calculate the number of unique paths to the right cell and the cell below
                curr_row[c] = curr_row[c + 1] + prev_row[c]
            # Update the previous row to be the current row
            prev_row = curr_row

        # The number of unique paths from the top-left to the bottom-right corner
        return prev_row[0]
        