class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        l,r = 1, num//2+1
        while l<r:
            m = l + (r-l)//2
            pow = m**2
            if pow == num:
                return True
            elif pow < num:
                l = m+1
            else:
                r = m
        return False