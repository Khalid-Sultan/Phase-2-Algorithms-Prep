class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row_i, row in enumerate(matrix):
            for col_i, col in enumerate(row):
                if col == "0":
                    dp[row_i][col_i] = 0
                else:
                    dp[row_i][col_i] = self.find(col_i, row)
        mx = 0
        print(dp)
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                mx = max(mx, self.search(dp, i, j))
        return mx

    def search(self, dp, start_row, start_col):
        start, up, down = dp[start_row][start_col], 0, 0
        if start_row > 0:
            for i in range(start_row - 1, -1, -1):
                if start <= dp[i][start_col]:
                    up += 1
                else:
                    break
        if start_row < len(dp) - 1:
            for i in range(start_row + 1, len(dp)):
                if start <= dp[i][start_col]:
                    down += 1
                else:
                    break
        return start * (up + down + 1)

    def find(self, index, row):
        count = 0
        for i in range(index, len(row)):
            if row[i] == "0":
                break
            count += 1
        return count