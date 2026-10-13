class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kb = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in kb.items():
            bucket[val].append(key)
        
        res = []
        for count in range(len(nums), 0, -1):
            for x in bucket[count]:
                res.append(x)
                if len(res) == k:
                    return res

        
        