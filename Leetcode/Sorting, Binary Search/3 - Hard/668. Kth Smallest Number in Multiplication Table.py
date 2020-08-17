class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(limit):
            ct = 0
            for i in range(1, m + 1):
                j = min(limit // i, n)
                if j == 0: break
                ct += j
            return ct >= k
        l, r = 1, m * n
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l
