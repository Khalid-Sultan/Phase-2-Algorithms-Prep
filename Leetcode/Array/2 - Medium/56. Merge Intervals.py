class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals, key=lambda start: start[0])
        res = []
        for i in s:
            if not res or (res and res[-1][1]<i[0]):
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res