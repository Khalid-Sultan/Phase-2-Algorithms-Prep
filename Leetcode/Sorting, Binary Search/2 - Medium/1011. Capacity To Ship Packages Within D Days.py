class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(capacity)->bool:
            total = 1
            s = 0
            for i in weights:
                s+=i
                if s>capacity:
                    total+=1
                    s = i
                    if total>D:
                        return False
            return True
        l = 0
        r = 0
        for i in weights:
            l = max(l, i)
            r+=i
        while l<r:
            m = l+(r-l)//2
            if check(m):
                r = m
            else:
                l = m+1
        return l