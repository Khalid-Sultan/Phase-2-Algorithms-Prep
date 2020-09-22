from collections import deque
class Solution:
    def makeGood(self, s: str) -> str:
        buffer = deque()
        for i in s:
            if len(buffer)>0 and ord(buffer[-1]) ^ ord(i) ==32:
                buffer.pop()
            else:
                buffer.append(i)
        return ''.join(buffer)
    