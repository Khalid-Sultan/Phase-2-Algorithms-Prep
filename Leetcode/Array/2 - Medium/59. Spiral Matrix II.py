class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [['x' for i in range(n)] for j in range(n)]
        directions = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]
        i = dt = r = c = d = 0
        while i < n * n:
            if d == 4: break
            if matrix[r][c] != 'x':
                r2 = r + directions[dt][0]
                c2 = c + directions[dt][1]
                if r2 < 0 or r2 >= n or c2 < 0 or c2 >= n or matrix[r2][c2] != 'x':
                    dt = (dt + 1) % 4
                    d += 1
                else:
                    r, c = r2, c2
                continue
            d = 0
            matrix[r][c] = i + 1
            i += 1

            r2 = r + directions[dt][0]
            c2 = c + directions[dt][1]
            if r2 < 0 or r2 >= n or c2 < 0 or c2 >= n or matrix[r2][c2] != 'x':
                dt = (dt + 1) % 4
                d += 1
            else:
                r, c = r2, c2

        return matrix

