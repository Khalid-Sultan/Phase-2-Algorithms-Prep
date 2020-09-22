class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # l,r = len(grid), len(grid[0])
        # res = 0
        # for i in range(l):
        #     for j in range(r):
        #         if grid[i][j]==1:
        #             #Do a search over all four directions
        #             self.dfs(grid, i, j)        
        #         if grid[i][j]==2:
        #             res+=1
        # return res

        l,r = len(grid), len(grid[0])
        res = 0
        s = set()
        row_servers, col_servers = [0] * l, [0] * r
        for i in range(l):
            for j in range(r):
                if grid[i][j] == 1:
                    s.add((i, j))
                    row_servers[i] += 1
                    col_servers[j] += 1
        for point in s:
            if row_servers[point[0]] > 1 or col_servers[point[1]] > 1:
                res += 1
        return res

    def dfs(self, grid, r, c):
        directions = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1],
        ]
        for i in directions:
            row, col = r, c
            while 0<=row+i[0]<len(grid) and 0<=col+i[1]<len(grid[0]):
                if grid[row+i[0]][col+i[1]]!=0:
                    grid[r][c]=2
                    grid[row+i[0]][col+i[1]]=2
                row+=i[0]
                col+=i[1]