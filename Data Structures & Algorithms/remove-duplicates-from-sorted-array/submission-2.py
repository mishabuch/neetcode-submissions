class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
        nums[:len(result)] = sorted(list(result))
        return len(list(result))
        