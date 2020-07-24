class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ret = [[] for i in range(100)]
        for ind,row in enumerate(mat):
            count = 0
            for col in row:
                if col==1:
                    count+=1
            ret[count].append(ind)
        ls = []
        for i in ret:
            for j in i:
                if k>0:
                    ls.append(j)
                    k-=1
        return ls
        