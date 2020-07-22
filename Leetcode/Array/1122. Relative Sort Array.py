class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ls = [0] * 1001
        for i in arr2:
            ls[i]+=1
        for i in arr1:
            ls[i]-=1
        res = []
        for i, ind in enumerate(arr2):
            res.append(ind)
            while ls[ind]<0:
                res.append(ind)
                ls[ind]+=1
        for i,ind in enumerate(ls):
            while ind<0:
                res.append(i)
                ind+=1
        return res
