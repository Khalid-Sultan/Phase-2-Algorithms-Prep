class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        s = set(tuple([i[0], i[1]]) for i in queens)
        r = []
        directions = [
            [1,0], [-1,0],
            [0,1], [0,-1],
            [1,1], [1,-1], [-1,1], [-1,-1]
        ]        
        for d in directions:
            t = self.check(s, d, king[0], king[1])
            if t!=None:
                r = r + [t]
        return r
    def check(self, s, direction, row, col):
        while row>=0 and col>=0 and row<=7 and col<=7:
            if tuple([row+direction[0], col+direction[1]]) in s:
                return [row+direction[0], col+direction[1]]
            row += direction[0]
            col += direction[1]
            