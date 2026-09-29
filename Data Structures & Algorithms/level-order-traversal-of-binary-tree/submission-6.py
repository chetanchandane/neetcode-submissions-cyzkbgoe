# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = []
        q = deque([root])
        while q:
            current = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    current.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if current:
                res.append(current)
            level += 1
        return res
        