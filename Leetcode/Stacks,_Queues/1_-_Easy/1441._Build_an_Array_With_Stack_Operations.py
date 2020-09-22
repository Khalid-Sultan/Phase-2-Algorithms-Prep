from collections import deque
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        buffer = deque()
        for i in range(n, 0, -1):
            buffer.append(i)
        for i in target:
            while buffer:
                res.append("Push")
                if buffer[-1]==i:
                    buffer.pop()
                    break
                res.append("Pop")
                buffer.pop()
        return res