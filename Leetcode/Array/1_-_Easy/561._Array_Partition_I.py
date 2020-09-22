class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = [0] * 20001
        for i in nums:
            n[i+10000]+=1
        sum = 0
        check = True
        for ind, i in enumerate(n):
            if i==0:
                continue            
            while i>0:
                if check:
                    sum += ind-10000
                    check = False
                else:
                    check = True
                i -= 1
        return sum