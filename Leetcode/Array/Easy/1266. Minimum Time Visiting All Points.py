class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        moves = self.recur(points, points[0], 1, 0)
        return moves
    def recur(self,points, start, index, moves):        
        if start[0]==points[index][0] and start[1]==points[index][1]:
            if index==len(points)-1:
                return moves
            return self.recur(points, points[index], index+1, moves)
        
        if start[0]==points[index][0]:
            if start[1]<points[index][1]:
                start[1] += 1
                return self.recur(points, start, index, moves+1)
            start[1] -= 1
            return self.recur(points, start, index, moves+1)

        if start[1]==points[index][1]:
            if start[0]<points[index][0]:
                start[0] += 1
                return self.recur(points, start, index, moves+1)
            start[0] -= 1
            return self.recur(points, start, index, moves+1)

        if start[0]<points[index][0]:
            start[0] += 1
            if start[1]<points[index][1]:
                start[1] += 1
                return self.recur(points, start, index, moves+1)
            start[1] -= 1
            return self.recur(points, start, index, moves+1)

        if start[0]>points[index][0]:
            start[0] -= 1
            if start[1]<points[index][1]:
                start[1] += 1
                return self.recur(points, start, index, moves+1)
            start[1] -= 1
            return self.recur(points, start, index, moves+1)

        return moves