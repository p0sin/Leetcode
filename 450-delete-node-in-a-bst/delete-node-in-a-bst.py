# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # FIND MIN FUNCTION
    def findMin(self, root):
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # CASE 1
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # CASE 2
                root.val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, root.val)

        return root




        