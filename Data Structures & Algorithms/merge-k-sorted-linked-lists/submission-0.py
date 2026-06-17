# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        l1 = []

        for root in lists:
            curr = root
            while curr:
                l1.append(curr.val)
                curr = curr.next

        l1.sort()

        dummy = ListNode()
        curr = dummy

        for i in range(len(l1)):
            n = ListNode(l1[i])
            curr.next = n
            curr = curr.next


        return dummy.next
        


        