class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(previous_rows, used_columns, current_col):
            if current_col in used_columns:
                return False
            start = len(previous_rows) - 1
            left_check = current_col - 1
            right_check = current_col + 1
            while start > -1:
                if left_check > -1 and previous_rows[start][left_check] == 'Q':
                    return False
                if right_check < len(previous_rows[start]) and previous_rows[start][right_check] == 'Q':
                    return False
                left_check -= 1
                right_check += 1
                start -= 1
            return True

        def dfs(temp, visited_columns, queens):
            nonlocal res
            if queens == n:
                res.append(temp)
                return
            for i in range(len(temp[-1])):
                start = ['.'] * n
                start[i] = 'Q'
                start = ''.join(start)
                if check(temp, visited_columns, i):
                    visited_columns.add(i)
                    dfs(temp + [start], visited_columns, queens + 1)
                    visited_columns.remove(i)

        res = []
        for i in range(n):
            start = ['.'] * n
            start[i] = 'Q'
            start = ''.join(start)
            dfs([start], {i}, 1)
        return res

