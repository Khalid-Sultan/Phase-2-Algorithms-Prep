class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        buffer = deque()
        ctr = 0
        for i in s:
            if buffer and buffer[-1][0]==i:
                ctr = buffer[-1][1]+1
            else:
                ctr =1
            buffer.append([i,ctr])
            if buffer[-1][1]>=k:
                ct = 0
                while ct<k and buffer:
                    buffer.pop()
                    ct+=1
        res = ""
        while buffer:
            res+=buffer.popleft()[0]
        return res

                