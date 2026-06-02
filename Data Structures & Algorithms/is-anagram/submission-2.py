class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i, char in enumerate(s):
            s_dict[char] = s.count(char)
        for i, char in enumerate(t):
            t_dict[char] = t.count(char)
        if s_dict==t_dict:
            return True
        return False
        