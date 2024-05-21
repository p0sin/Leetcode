# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        path = []
        return self.backTracking(root, targetSum, path)
       
    def backTracking(self, root, targetSum, path):
        if not root:
            return False

        path.append(root.val)
        if root.left is None and root.right is None and sum(path) == targetSum:
            return True
        if self.backTracking(root.left, targetSum, path):
            return True
        if self.backTracking(root.right, targetSum, path):
            return True
        path.pop()
        return False

    