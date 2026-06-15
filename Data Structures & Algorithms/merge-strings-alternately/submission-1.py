class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        iter = min(len(word1), len(word2))
        for i in range(iter):
            res += word1[i] + word2[i]
        if len(word1) < len(word2):
            res += word2[iter:] 
        else:
            res += word1[iter:] 
        return res
        