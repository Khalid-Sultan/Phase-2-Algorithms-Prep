class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j]<=prices[i]:
#                     prices[i] -= prices[j]
#                     break
#         return prices
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A