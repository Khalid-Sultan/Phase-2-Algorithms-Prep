class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = [0]*len(A)
        ind = 0
        end = len(A)-1
        for i in A:
            if i%2==0:
                ans[ind] = i
                ind += 1
            else:
                ans[end] = i
                end -= 1
        return ans