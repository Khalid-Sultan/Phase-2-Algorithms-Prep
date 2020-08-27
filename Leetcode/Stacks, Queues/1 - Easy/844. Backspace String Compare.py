from collections import deque
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        deque_1 = deque()
        deque_2 = deque()
        for i in S:
            if i == '#':
                if len(deque_1)>0:
                    deque_1.pop()
            else:
                deque_1.append(i)
        for i in T:
            if i == '#':
                if len(deque_2)>0:
                    deque_2.pop()
            else:
                deque_2.append(i)
        if len(deque_1)!=len(deque_2): return False
        while len(deque_1)>0:
            if deque_1.pop()!=deque_2.pop():
                return False
        return True