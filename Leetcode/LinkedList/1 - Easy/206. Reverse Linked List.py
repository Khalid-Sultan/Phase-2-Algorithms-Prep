# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev, nxt, current = None,None, head
        # while current!=None:
        #     nxt = current.next
        #     current.next = prev
        #     prev = current
        #     current = nxt
        # return prev
        return recur(head)

    def recur(self, head: ListNode) -> ListNode:
        if head == None or head.next==None:
            return head
        revHead = recur(head.next)
        head.next.next = head
        head.next = None
        return revHead