class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = (l + r) // 2
            midRow, midCol = mid // cols, mid % cols

            if matrix[midRow][midCol] < target:
                l = mid + 1
            elif matrix[midRow][midCol] > target:
                r = mid - 1
            else:
                return True

        return False
        