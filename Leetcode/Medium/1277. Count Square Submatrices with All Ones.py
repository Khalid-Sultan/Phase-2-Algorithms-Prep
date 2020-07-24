class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None:
            return 0
        if len(matrix) == 0:
            return 0
        c = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                curr = matrix[row][col]
                if curr == 1:
                    if row == 0:
                        c += 1
                    elif col == 0:
                        c += 1
                    else:
                        _min = min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1]) + curr
                        c += _min
                        matrix[row][col] = _min
        return c