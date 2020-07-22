class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        out = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i]>max:
                max = arr[i]
            out.insert(0,max)
        out.append(-1)
        return out[1:]
