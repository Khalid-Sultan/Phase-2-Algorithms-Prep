class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # col_end, row_end = -1, -1
        # col_start, row_start = len(grid[0])-1, len(grid)-1
        # count = 0
        # for i in range(row_start, row_end, -1):
        #     if col_end==0 and grid[i][0]>=0:
        #         row_end = i
        #     for j in range(col_start, col_end, -1):
        #         if grid[i][j]<0:
        #             count += 1
        #             continue
        #         col_end = j
        # return count

        row_start, col_start, count = len(grid)-1, 0, 0
        while row_start > -1 and col_start<len(grid[0]):
            if grid[row_start][col_start]>=0:
                col_start += 1
            else:
                row_start -=1
                count += len(grid[0]) - col_start
        return count