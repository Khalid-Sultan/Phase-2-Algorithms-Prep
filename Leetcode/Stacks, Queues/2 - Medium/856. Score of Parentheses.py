class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # stack = deque()
        # for i in S:
        #     if i=='(':
        #         stack.append(i)
        #     else:
        #         if stack[-1]=='(':
        #             stack.pop()
        #             stack.append(1)
        #         else:
        #             s = 0
        #             while stack and stack[-1]!='(':
        #                 s+=stack.pop()
        #             stack.pop()
        #             stack.append(2*s)
        # s = 0
        # print(stack)
        # while stack and stack[-1]!='(':
        #     s+=stack.pop()
        # return s
        stack = deque()
        stack.append(0)
        for i in S:
            if i=='(':
                stack.append(0)
            else:
                depth = stack.pop()
                stack[-1]+=max(1, 2*depth)
        return stack[-1]