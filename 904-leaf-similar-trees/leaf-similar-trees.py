# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(sequence, root):
            if root is None:
                return

            if root.left is None and root.right is None:
                sequence.append(root.val)
                return

            dfs(sequence, root.left)
            dfs(sequence, root.right)


        seq1, seq2 = [], []

        dfs(seq1, root1)
        dfs(seq2, root2)

        return seq1 == seq2

            

        

        



        
        