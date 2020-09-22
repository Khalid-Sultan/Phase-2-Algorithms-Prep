class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        #Use binary search 
        l,r = 0, len(A)
        while l<r:
            m = (l + r)//2
            if A[m]<A[m+1]:
                l = m+1
            else:
                r = m
        return l