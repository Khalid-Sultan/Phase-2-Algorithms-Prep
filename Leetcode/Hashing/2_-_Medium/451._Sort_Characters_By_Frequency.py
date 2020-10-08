class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i]+=1
        res = [0]*len(s)
        ctr = 0
        for w in sorted(d, key=d.get, reverse=True):
            while d[w]>0:
                res[ctr] = w
                d[w]-=1
                ctr+=1
        return "".join(res)