class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        for r_idx, row in enumerate(matrix):
            total = 0
            for c_idx, val in enumerate(row):
                total += val
                self.prefix[r_idx][c_idx] = total
        print(f"{self.prefix}")

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumRegion = 0
        for i in range(row1, row2+1):
            if col1 > 0:
                sumRegion += self.prefix[i][col2] - self.prefix[i][col1-1]
            else:
                sumRegion += self.prefix[i][col2]
        return sumRegion


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)