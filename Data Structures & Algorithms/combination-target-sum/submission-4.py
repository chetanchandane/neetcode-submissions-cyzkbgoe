class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            for i in range(ind, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr, total + nums[i])
                curr.pop()


        backtrack(0, [], 0)
        return res