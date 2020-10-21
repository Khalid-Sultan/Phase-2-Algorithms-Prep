class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0]*len(colSum) for i in range(len(rowSum))]
        row_start = col_start = 0
        while row_start<len(rowSum) and col_start<len(colSum):
            smaller = min(rowSum[row_start], colSum[col_start])
            matrix[row_start][col_start] = smaller
            rowSum[row_start]-=smaller
            colSum[col_start]-=smaller
            row_start = row_start+1 if rowSum[row_start]==0 else row_start
            col_start = col_start+1 if colSum[col_start]==0 else col_start
        return matrix