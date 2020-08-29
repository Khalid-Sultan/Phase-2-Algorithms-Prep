from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         stack = deque()
#         moved = 1
#         ptr = ptr2 = 0
#         while moved==1:
#             if moved==0:
#                 break
#             moved = 0
#             if not stack and ptr2<len(pushed):
#                 stack.append(pushed[ptr2])
#                 ptr2+=1
#                 moved = 1
#             while stack and stack[-1]!=popped[ptr] and ptr2<len(pushed):
#                 stack.append(pushed[ptr2])
#                 ptr2+=1
#                 moved = 1
# t
#             if ptr<len(popped) and stack and stack[-1]==popped[ptr]:
#                 ptr+=1
#                 stack.pop()
#                 moved = 1
#         return len(stack) == 0
        stack = deque()
        popped_stack = deque()
        for i in popped:
            popped_stack.appendleft(i)
        for i in pushed:
            if i!=popped_stack[-1]:
                stack.append(i)
            else:
                popped_stack.pop()
                while stack and stack[-1]==popped_stack[-1]:
                    stack.pop()
                    popped_stack.pop()
        return len(stack)==0