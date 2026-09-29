# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level = 0
        res = []
        q = deque([root])
        while q:
            res.append([])
            for _ in range(len(q)):
                node = q.popleft()
                res[level].append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return res
        