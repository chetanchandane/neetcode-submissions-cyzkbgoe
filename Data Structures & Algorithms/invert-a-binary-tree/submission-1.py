# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invert(node):
            if not node:
                return None
            left_child = node.left
            right_child = node.right
            node.left, node.right = right_child, left_child
            _invert(node.left)
            _invert(node.right)


        _invert(root)
        return root