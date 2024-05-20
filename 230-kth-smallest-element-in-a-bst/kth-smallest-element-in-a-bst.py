# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        values = []
        self.inOrder(root, values)
        return values[k - 1]
        

    def inOrder(self, root, values):
        if root is None:
            return

        self.inOrder(root.left, values)
        values.append(root.val)
        self.inOrder(root.right, values)
        