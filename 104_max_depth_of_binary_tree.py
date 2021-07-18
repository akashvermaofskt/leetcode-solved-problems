# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, depth=0):
            nonlocal ans
            if node:
                ans = max(ans, depth + 1)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)
        return ans
