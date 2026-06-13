class Solution: 
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        res = 1
        for num in nums:
            if num > 0:
                if num == res:
                    res += 1
                elif num > res:
                    break
        
        return res
