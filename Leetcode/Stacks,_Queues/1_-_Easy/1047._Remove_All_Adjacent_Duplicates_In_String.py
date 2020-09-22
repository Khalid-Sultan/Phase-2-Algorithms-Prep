from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        buffer = deque()
        for i in S:
            if buffer and buffer[-1]==i:
                buffer.pop()
            else:
                buffer.append(i)
        return "".join(buffer)