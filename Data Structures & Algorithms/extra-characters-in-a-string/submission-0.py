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
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]


        