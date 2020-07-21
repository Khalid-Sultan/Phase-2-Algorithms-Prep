class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [x*x for x in A]
        A.sort()
        return A