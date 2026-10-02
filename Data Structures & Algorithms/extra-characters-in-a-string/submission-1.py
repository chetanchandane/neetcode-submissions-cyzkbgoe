class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.add(w)
        n = len(s)
        dp = {len(s): 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1) #skip the current char
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        return dfs(0)

        


        