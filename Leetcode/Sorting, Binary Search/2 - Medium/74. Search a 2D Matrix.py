class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0: return False
        #Search for appropriate row then for appropriate column
        t,b = 0, len(matrix)
        while t<b:
            m = t + (b-t)//2
            if target<=matrix[m][-1]:
                b = m
            else:
                t = m+1
        if t>=len(matrix): return False
        l,r = 0, len(matrix[0])-1
        while l<=r:
            mid = l + (r-l)//2
            if target==matrix[t][mid]:
                return True
            elif target<matrix[t][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False