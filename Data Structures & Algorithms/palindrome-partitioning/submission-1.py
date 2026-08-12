class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            dp[i][i+1] = (s[i]==s[i+1])
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length -1
                dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]
        res = []
        def backtrack(s, index, path):
            if index >= len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if dp[index][i]:
                    path.append(s[index:i+1])
                    backtrack(s, i+1, path)
                    path.pop()

        backtrack(s, 0, [])
        return res
