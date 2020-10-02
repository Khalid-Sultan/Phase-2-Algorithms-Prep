class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            pos = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        mx = 1<<31
        if divisor==dividend: return pos
        if divisor==1:
            res = pos*dividend
            return res if res<mx else mx-1
        if divisor>dividend: return 0
        left = 1
        right = dividend
        while left<right:
            mid = left + (right-left)//2
            s = self.russianPeasant(mid,divisor)
            if s==dividend:
                return pos*mid
            elif s>dividend:
                right = mid
            else:
                left = mid+1
            print(left, right)
        left-=1
        res = pos*left
        return res if res<mx else mx-1

    def russianPeasant(self,a,b):
        res = 0 # initialize result
        # While second number doesn't
        # become 1
        while (b > 0):
            # If second number becomes
            # odd, add the first number
            # to result
            if (b & 1):
                res = res + a
            # Double the first number
            # and halve the second
            # number
            a = a << 1
            b = b >> 1
        return res