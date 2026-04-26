# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(node):
            curr = node
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        rev = reverse(head)

        dummy = ListNode(0, rev)
        curr = dummy
        count = 0

        while curr and count < n-1:
            curr = curr.next
            count += 1
        

        curr.next = curr.next.next
        

        return reverse(dummy.next)

            


        