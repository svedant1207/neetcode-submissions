# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        n = []
        curr = head

        while curr:
            n.append(curr)
            curr = curr.next

        i, j = 0, len(n) - 1

        while i < j:
            n[i].next = n[j]
            i += 1

            if i == j:
                break

            n[j].next = n[i]
            j -= 1

        n[i].next = None