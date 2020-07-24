class Solution:
    def __init__(self):
        super().__init__()
    def diagonalSort(self, mat: [[]]) -> [[]]:
        row_indices = range(len(mat))
        col_indices = range(len(mat[0]))
        for i in row_indices:
            row,col = i,0
            start = mat[row][col]
            end_row = len(mat)-1
            end_col = len(mat[0])-1
            l = [start]
            while row<end_row and col<end_col:
                l.append(mat[row+1][col+1])
                row, col = row+1, col+1
            c = [0] * 100
            for j in l:
                c[j - 1] += 1
            k = []
            for ind,j in enumerate(c):
                while j > 0:
                    k.append(ind+1)
                    j -= 1
            row, col = i, 0
            z = 0
            mat[row][col] = k[z]
            end_row = len(mat)-1
            end_col = len(mat[0])-1
            while row<end_row and col<end_col:
                mat[row+1][col+1] = k[z+1]
                row, col = row + 1, col + 1
                z+=1
        for i in col_indices:
            row,col = 0,i
            start = mat[row][col]
            end_row = len(mat)-1
            end_col = len(mat[0])-1
            l = [start]
            while row<end_row and col<end_col:
                l.append(mat[row+1][col+1])
                row, col = row+1, col+1
            c = [0] * 100
            for j in l:
                c[j - 1] += 1
            k = []
            for ind,j in enumerate(c):
                while j > 0:
                    k.append(ind+1)
                    j -= 1
            row, col = 0, i
            z = 0
            mat[row][col] = k[z]
            end_row = len(mat)-1
            end_col = len(mat[0])-1
            while row<end_row and col<end_col:
                mat[row+1][col+1] = k[z+1]
                row, col = row + 1, col + 1
                z+=1
        return mat
if __name__ == "__main__":
    a = Solution()
    l = [[3, 3, 1, 1],[2, 2, 1, 2],[1, 1, 1, 2]]
    print(a.diagonalSort(l))