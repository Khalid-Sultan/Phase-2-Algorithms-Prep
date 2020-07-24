class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 0
        for i in range(1, len(A), 2):
            if A[i]%2==0:
                while A[j]%2==0:
                    j+=2
                A[i],A[j] = A[j],A[i]
        return A
