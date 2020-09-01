# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # s = 0
        # y = 0
        # temp = head
        # while temp:
        #     temp = temp.next
        #     if temp: y+=1
        # while head:
        #     if head.val==1:
        #         s += 1 << y
        #     head = head.next
        #     y-=1
        # return s

        # s = 0
        # while head:
        #     s *= 2
        #     s += head.val
        #     head = head.next
        # return s
        
        s = 0
        while head:
            print('Before', s, head.val)
            s = (s<<1) | head.val
            print('After', s, head.val)
            head = head.next
        return s