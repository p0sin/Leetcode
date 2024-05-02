# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return

        if root.left is None and root.right is None:
            return root
        
        tempNode = TreeNode()
        tempNode = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tempNode

        return root
        