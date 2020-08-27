class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0, n
        while l<=r:
            m = l + (r-l)//2
            s = (m * (m+1))/2
            if s<n:
                l = m+1
            elif s>n:
                r = m-1
            else:
                return m
        return r
