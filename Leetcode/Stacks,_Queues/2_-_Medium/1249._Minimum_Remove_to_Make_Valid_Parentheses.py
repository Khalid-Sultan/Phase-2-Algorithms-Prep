from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # buffer = deque()
        # res = deque()
        # for ind, i in enumerate(s):
        #     if i=='(':
        #         buffer.append((i,ind))
        #     elif i==')':
        #         if buffer and buffer[-1][0]=='(':
        #             buffer.pop()
        #         else:
        #             buffer.append((i,ind))
        # for i in range(len(s)-1, -1, -1):
        #     if buffer and buffer[-1][1]==i:
        #         buffer.pop()
        #     else:
        #         res.appendleft(s[i])
        # return "".join(res)
        stack = deque()
        res = [''] * len(s)
        for ind, i in enumerate(s):
            if i == '(':
                stack.append(ind)
            elif i == ')':
                if stack:
                    c = stack.pop()
                    res[ind] = i
                    res[c] = s[c]
            else:
                res[ind] = i
        return "".join(res)