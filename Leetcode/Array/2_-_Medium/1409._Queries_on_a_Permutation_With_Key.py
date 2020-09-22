class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1,m+1)]
        ret = []
        for i in queries:
            ind = P.index(i)
            P.remove(i)
            P.insert(0,i)
            ret.append(ind)
        return ret
    