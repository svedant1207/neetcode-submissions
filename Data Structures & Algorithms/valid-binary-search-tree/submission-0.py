# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        curr = root
        stk2 = []

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            curr = stk.pop()
            stk2.append(curr.val)

            curr = curr.right

        for i in range(1, len(stk2)):
            if stk2[i] <= stk2[i - 1]:
                return False

        return True
        
        