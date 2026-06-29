# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(head)
        tail = dummy

        curr = head
        while curr:
            tail.next = ListNode(curr.val)
            tail = tail.next
            curr = curr.next
        
        curr = dummy.next
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        p1 = head
        p2 = prev

        while p1:
            if p1.val != p2.val:
                return False
            
            p1 = p1.next
            p2 = p2.next

        
        return True
        



        