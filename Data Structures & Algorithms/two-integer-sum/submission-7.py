class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in cache:
                return [cache[rem], i]
            cache[nums[i]]=i

        



            