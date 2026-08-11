class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, curr):
            res.append(curr.copy())
            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res