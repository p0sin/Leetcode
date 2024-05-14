# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                count[0] += 1
                maxVal = node.val

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        count = [0]
        dfs(root, root.val)

        return count[0]
        
        