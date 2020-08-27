from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        buffer = deque()
        for i in s:
            if buffer:
                if buffer[-1]=="[" and i=="]":
                    buffer.pop()
                elif buffer[-1]=="(" and i==")":
                    buffer.pop()
                elif buffer[-1]=="{" and i=="}":
                    buffer.pop()
                else:
                    buffer.append(i)
            else:
                buffer.append(i)
        return len(buffer)==0            