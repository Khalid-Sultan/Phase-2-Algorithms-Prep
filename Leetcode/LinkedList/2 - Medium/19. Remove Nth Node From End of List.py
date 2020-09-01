# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        c = 0
        while head:
            d[c] = head
            c+=1
            head = head.next
        if c==n:
            if 1 in d: return d[1]
            return None
        last = c-n-1
        if last<0:
            return None
        d[last].next = d[last+1].next if last+1 in d else None
        return d[0]