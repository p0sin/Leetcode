class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = { i: [] for i in range(len(board))}
        rows = { i: [] for i in range(len(board))}
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                current = board[r][c]

                if current != ".":
                    # Check for rows
                    if current in rows[r]:
                        return False    
                    rows[r].append(current)
                        
                    # Append to Columns
                    if current in columns[c]:
                        return False
                    columns[c].append(current)

                    # Check in boxes
                    if current in boxes[(r // 3, c // 3)]:
                        return False
                    boxes[(r // 3, c // 3)].add(current)
                 
        return True

        
        