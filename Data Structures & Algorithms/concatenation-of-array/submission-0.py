class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for k in range(0,2):
            for i in nums:
                answer.append(i)
        print(answer)
        return answer
        