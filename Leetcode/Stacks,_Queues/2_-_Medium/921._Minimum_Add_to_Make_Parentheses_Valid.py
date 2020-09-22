from collections import deque
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
#         buffer = deque()
#         for i in S:
#             if i==")":
#                 if buffer and buffer[-1]=="(":
#                     buffer.pop()
#                 else:
#                     buffer.append(i)
#             else:
#                 buffer.append(i)
#         return len(buffer)
        l = r = 0
        for i in S:
            if i==")":
                if l==0: r+=1
                else: l-=1
            else: l+=1
        return l+r