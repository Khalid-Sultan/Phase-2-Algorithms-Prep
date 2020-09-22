class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def trace(matrix, limit):
            count = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]<=limit:
                        count += 1
                    if matrix[i][0]>limit and matrix[i][j]>limit:
                        return count
            return count
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            count = trace(matrix, mid)
            if count >= k:
                r = mid
            else:
                l = mid + 1
        return l
    