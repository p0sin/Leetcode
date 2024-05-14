# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [root]
        maxLevel, level, maxSum = 1, 1, float('-inf')
        
        while q:
            levelSum = 0
            nextLevel = []

            for node in q:
                levelSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if levelSum > maxSum:
                maxLevel = level
                maxSum = levelSum

            level += 1
            q = nextLevel
            
        return maxLevel
        