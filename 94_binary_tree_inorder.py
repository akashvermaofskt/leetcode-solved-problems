# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node):
        if node:
            inorder(node.left)
            self.ans.append(node.val)
            inorder(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        inorder(root)
        return self.ans
