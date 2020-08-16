class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def check(capacity)->bool:
            hours = 0
            for i in piles:
                if i%capacity==0:
                    hours += i/capacity
                else:
                    hours += i//capacity + 1
            return hours<=H
        l = 1
        r = 0
        for i in piles:
            r = max(r, i)
        while l<r:
            m = l + (r-l)//2
            if check(m):
                r = m
            else:
                l = m+1
        return l