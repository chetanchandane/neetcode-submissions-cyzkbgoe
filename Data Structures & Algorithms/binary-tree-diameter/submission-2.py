# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            res = max(res, leftmax+rightmax)
            return 1 + max(leftmax, rightmax)
        dfs(root)
        return res

