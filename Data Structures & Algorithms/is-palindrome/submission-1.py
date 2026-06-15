class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([char for char in s if char.isalnum()]).lower()
        res = False
        if len(cleaned) == 0 or len(cleaned)==1:
            return True
        for i, val in enumerate(cleaned):
            j = len(cleaned) - i - 1
            print(f"i is {i} and j is {j}")
            if j > i:
                if cleaned[i] == cleaned[j]:
                    res = True
                else:
                    return False
        return res



        