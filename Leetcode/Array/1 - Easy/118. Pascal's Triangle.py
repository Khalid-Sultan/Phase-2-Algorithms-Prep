class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0: return []
        ret = [[1]]
        for i in range(numRows-1):
            ls = [1]
            for j in range(1, len(ret[-1])):
                ls.append(ret[-1][j] + ret[-1][j-1])
            ls.append(1)
            ret.append(ls)
        return ret
                