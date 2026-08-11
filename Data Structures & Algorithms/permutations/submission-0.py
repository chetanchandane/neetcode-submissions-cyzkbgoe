class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False]*len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    used[i] = False
                    
        
        backtrack([])
        return res