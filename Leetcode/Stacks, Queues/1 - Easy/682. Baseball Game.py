from collections import deque
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        buffer = deque()
        sums = 0
        for i in ops:
            print(sums)
            if i=="C":
                if buffer:
                    sums -= buffer.pop()
            elif i=="D":
                if buffer:
                    buffer.append(2 * buffer[-1])
                    sums += buffer[-1]
            elif i=="+":
                c = 0
                one = two = None
                if buffer: 
                    two = buffer.pop()
                    c+=two
                if buffer: 
                    one = buffer.pop()
                    c+=one
                if one: buffer.append(one)
                if two: buffer.append(two)
                if buffer: buffer.append(c)
                sums += c
            else:
                buffer.append(int(i))
                sums += int(i)
        return sums
