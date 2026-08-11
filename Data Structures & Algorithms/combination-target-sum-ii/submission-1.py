class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(ind, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return res