# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if not p or not q or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # stack = [(p, q)]
        # while stack:
        #     n1, n2 = stack.pop()
        #     if not n1 and not n2:
        #         continue
        #     if not n1 or not n2 or n1.val != n2.val:
        #         return False
        #     stack.append((n1.left, n2.left))
        #     stack.append((n1.right, n2.right))
        # return True

        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            for _ in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()
                if not n1 and not n2:
                    continue
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
        return True