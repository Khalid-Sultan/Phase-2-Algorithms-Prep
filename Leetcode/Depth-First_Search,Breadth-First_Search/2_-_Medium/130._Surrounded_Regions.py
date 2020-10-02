class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=='O':
                    tobechanged = set()
                    check = self.dfs(board, row, col, tobechanged)
                    if check:
                        board[row][col] = 'X'
                        for i in tobechanged:
                            board[i[0]][i[1]] = 'X'
    def dfs(self, board, row, col, tobechanged):
        if (row,col) in tobechanged:
            return True
        if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
            return False
        if (row==0 or row==len(board)-1) and board[row][col]=='O':
            return False
        if (col==0 or col==len(board[0])-1) and board[row][col]=='O':
            return False
        if board[row][col]=='X':
            return True
        tobechanged.add((row,col))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        conclusion = True
        for i in directions:
            conclusion = conclusion and self.dfs(board, row+i[0], col+i[1], tobechanged)
        return conclusion