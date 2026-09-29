# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        # def dfs(node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return arr[k-1]
        # cnt = k
        # res = root.val
        # def dfs(node):
        #     nonlocal cnt, res
        #     if not node:
        #         return
        #     dfs(node.left)
        #     if cnt == 0:
        #         return
        #     cnt -= 1
        #     if cnt == 0:
        #         res = node.val
        #         return
        #     dfs(node.right)
        
        # dfs(root)
        # return res
        
        #iterative dfs
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

