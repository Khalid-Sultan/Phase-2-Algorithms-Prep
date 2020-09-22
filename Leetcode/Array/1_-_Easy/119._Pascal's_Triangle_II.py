class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]*(rowIndex+1)
        for i in range(rowIndex):
            for j in range(i,0,-1):
                ret[j] += ret[j-1]
        return ret