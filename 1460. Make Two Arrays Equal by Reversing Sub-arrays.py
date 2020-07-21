class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        n = [0] * 1000
        for i in target:
            n[i-1]+=1
        for j in arr:
            n[j-1]-=1
            if n[j-1]<0:
                return False
        return True