# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level = 0
        # res = []
        # q = deque([root])
        # while q:
        #     current = []
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             current.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if current:
        #         res.append(current)
        #     level += 1
        # return res

        # dfs
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res)==depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res
        