class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        d = {}
        for i in range(R):
            for j in range(C):
                dist = abs(i-r0) + abs(j-c0)
                if dist not in d:
                    d[dist] = []
                d[dist].append([i,j])
        a = []
        for key in sorted(d):
            a.extend(d[key])
        return a