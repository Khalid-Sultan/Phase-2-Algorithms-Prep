class Solution:
    def reverseParentheses(self, s: str) -> str:
        # buffer = deque()
        # for i in s:
        #     if i==')':
        #         temp = deque()
        #         while buffer and buffer[-1]!='(':
        #             temp.appendleft(buffer.pop())
        #         if buffer:
        #             buffer.pop()
        #         while temp:
        #             buffer.append(temp.pop())
        #     else:
        #         buffer.append(i)
        # return "".join(buffer)
        buffer = deque()
        tracker = {}
        for ind, i in enumerate(s):
            if i == '(':
                buffer.append(ind)
            elif i == ')':
                end = buffer.pop()
                tracker[ind], tracker[end] = end, ind
        res = []
        start, counter = 0, 1
        while start < len(s):
            if s[start] == '(' or s[start] == ')':
                start = tracker[start]
                counter = -counter
            else:
                res.append(s[start])
            start += counter
        return "".join(res)