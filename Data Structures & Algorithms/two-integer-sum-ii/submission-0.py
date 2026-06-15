class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        for i, val in enumerate(numbers):
            if (target - val) in numbers:
                index1 = i
                index2 = numbers.index((target - val))
                break
        return [index1+1,index2+1]

        