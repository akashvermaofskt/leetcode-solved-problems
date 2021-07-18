# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True

        def equal(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return equal(node1.left, node2.left) and equal(node1.right, node2.right)
            return False

        return equal(root.left, root.right)
