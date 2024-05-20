# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        def inOrder(root, output):
            if root is None:
                return

            inOrder(root.left, output)
            output.append(root.val)
            inOrder(root.right, output)

            return output

        return inOrder(root, output)

    