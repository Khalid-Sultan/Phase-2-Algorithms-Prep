from collections import deque
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        buffer = deque()
        left = right = 0
        res = ""
        for i in S:
            if i==")" and left == right+1:
                #clear the buffer and add the content to the resultant string
                res += "".join(buffer) 
                buffer = deque()
                left = right = 0
            else:
                if left>0:
                    buffer.append(i)
                if i == '(': left += 1
                else: right += 1
        return res