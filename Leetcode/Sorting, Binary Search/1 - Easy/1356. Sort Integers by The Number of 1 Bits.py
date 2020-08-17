class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        for i in arr:
            temp = []
            t = 0
            c = i
            while i>1:
                if i%2==0:
                    temp.append(0)
                    i/=2
                else:
                    temp.append(1)
                    t+=1
                    i= (i-1)/2
            temp.append(i)
            temp = temp[::-1]
            if t not in d:
                d[t] = []
            d[t].append(c)
        res = []
        for key in sorted(d):
            ls = sorted(d[key])
            res.extend(ls)
        return res