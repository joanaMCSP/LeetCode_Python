# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return 0
        depth_left = self.dfs(root.left)
        depth_right = self.dfs(root.right)
        max_depth = depth_left  if  depth_left >= depth_right else depth_right
        return 1 + max_depth
        
