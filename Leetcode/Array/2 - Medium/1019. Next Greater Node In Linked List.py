# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ret = [0]*len(ls)
        buffer = deque()
        for i in range(len(ls)):
            while buffer and ls[buffer[-1]]<ls[i]:
                ret[buffer.pop()] = ls[i]
            buffer.append(i)
        return ret
