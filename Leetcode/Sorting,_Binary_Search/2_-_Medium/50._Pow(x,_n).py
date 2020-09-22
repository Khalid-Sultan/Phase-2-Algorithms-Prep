class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        
        p=1
        if n<0:
            n *= -1
            p = -1
        
        l = 1
        while n:
            if n%2:
                l *=x
            x*=x
            n//=2
            
        return l if p==1 else 1/l
