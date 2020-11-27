class Solution:
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, (row, col), set(), 0):
                        return True
        return False

    def dfs(self, board, word, position, visited, start):
        directions = ((-1, 0), (+1, 0), (0, -1), (0, +1))
        row, col = position
        if start == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if position in visited:
            return False
        if board[row][col] != word[start]:
            return False
        visited.add(position)
        for dirn_row, dirn_col in directions:
            check = self.dfs(board, word, (row + dirn_row, col + dirn_col), visited, start + 1)
            if check:
                return True
        visited.remove(position)
        return False