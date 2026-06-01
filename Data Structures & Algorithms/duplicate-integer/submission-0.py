class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_duplicates = {}

        for i, val in enumerate(nums):
            hash_duplicates.setdefault(val, []).append(i)

        for val in nums:
            if len(hash_duplicates[val]) > 1:
                return True
        return False

        