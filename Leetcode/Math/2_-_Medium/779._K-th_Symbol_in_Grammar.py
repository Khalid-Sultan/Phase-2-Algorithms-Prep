class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # if N==1: return 0
        # choice = N-1//4
        # stack = deque()
        # stack.append(0)
        # stack.append(1)
        # for i in range(N-1):
        #     if len(stack)>K:
        #         break
        #     temp = copy.deepcopy(stack)
        #     while temp:
        #         stack.append(1 if temp.popleft()==0 else 0)
        # return stack[K-1]
        
        if N == 1: return 0
        row_size = 1<<N-1
        flipped = False
        while row_size>2:
            half = row_size//2
            #If K in second half
            if K>half:
                K -= half
                flipped = not flipped
            row_size = half
        K-=1
        if flipped:
            K = 1-K
        return K
        
