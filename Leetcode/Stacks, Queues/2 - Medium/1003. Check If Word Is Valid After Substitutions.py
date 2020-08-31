class Solution:
    def isValid(self, s: str) -> bool:
        buffer = deque()
        for i in s:
            if i=='c' and buffer:
                if buffer[-1]!="ab":
                    return False
                buffer.pop()
            elif i=='a':
                buffer.append('a')
            else:
                if buffer:
                    buffer[-1] = buffer[-1]+'b'
                else:
                    buffer.append('b')
        return len(buffer)==0