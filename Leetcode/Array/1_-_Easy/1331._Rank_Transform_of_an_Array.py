class Solution:
    def arrayRankTransform(self, arr2: List[int]) -> List[int]:
        d = {}
        if len(arr2)==0: return []
        ct = 1
        arr = sorted(arr2)
        d[arr[0]] = 1
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                ct+=1
            d[arr[i]] = ct
        res = [1] *len(arr)
        for ind,i in enumerate(arr2):
            if i in d:
                res[ind] = d[i]
        return res
