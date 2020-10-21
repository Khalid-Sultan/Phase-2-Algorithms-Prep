class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0: return [0]
        if num==1: return [0,1]
        res = [0]*(num+1)
        res[1] = 1
        res[2] = 1
        for i in range(3, num + 1):
            if i % 2 == 1:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i // 2]
        return res