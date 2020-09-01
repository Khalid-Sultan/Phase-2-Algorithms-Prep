# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#         ls = []
#         while head:
#             ls.append(head.val)
#             head=  head.next
#         l,r = 0, len(ls)-1
#         while l<r:
#             if ls[l]!=ls[r]: return False
#             l+=1
#             r-=1
#         return True
        count = 0
        temp = head
        while temp:
            temp= temp.next
            count+=1
        left = head
        right = head
        l = count//2
        if count%2!=0:
            l+=1
        while l>0:
            right = right.next
            l-=1
            
        #reverse the second half
        prev, nxt, current = None,None, right
        while current!=None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        right = prev
        while left!=right and left!=None and right!=None:
            if left.val!=right.val:
                return False
            left =  left.next
            right = right.next
        return True