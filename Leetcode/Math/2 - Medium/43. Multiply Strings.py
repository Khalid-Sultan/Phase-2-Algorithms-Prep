class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]*(len(num1)*len(num2)+1)
        end = len(res)-1
        for j in range(len(num2)-1,-1,-1):
            self.rec(num1, num2[j], res, end)
            end-=1
        start = 0
        for ind,i in enumerate(res):
            if i!=0:
                start = ind
                break
            start+=1
        if start>=len(res): return "0"
        res = [str(i) for i in res]
        return "".join(res[start:])
    def rec(self, a, b, res, start):
        # print(a,b,res,start)
        carry = 0
        for i in range(len(a)-1,-1,-1):
            product = res[start] + int(a[i])*int(b)+carry
            carry = product//10
            res[start] = product%10
            start-=1
        if carry:
            res[start] = carry