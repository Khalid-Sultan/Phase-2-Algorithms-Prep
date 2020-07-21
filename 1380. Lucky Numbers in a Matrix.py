class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_len, col_len = len(matrix), len(matrix[0])
        ls = []
        for row in range(0, row_len):
            min, ind = matrix[row][0], 0
            for col in range(0, col_len):
                if matrix[row][col]<min:
                    min = matrix[row][col]
                    ind = col
            for i in range(0, row_len):
                if matrix[i][ind]<=matrix[row][ind]:
                    continue
                else:
                    ind = -1
            if ind!=-1:
                ls.append(matrix[row][ind]) 
            
        return ls
