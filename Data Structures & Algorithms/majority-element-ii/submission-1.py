class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        items = [key for key, value in freq.items() if value > (len(nums)//3)]
        return items