class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        grid = [[0]*m for i in range(n)]
        count = 0
        for ind in indices:
            for i in range(n):
                grid[i][ind[1]] += 1
                count += 1 if grid[i][ind[1]]%2==1 else -1
            for i in range(m):
                grid[ind[0]][i] += 1
                count += 1 if grid[ind[0]][i]%2==1 else -1
        return count
    