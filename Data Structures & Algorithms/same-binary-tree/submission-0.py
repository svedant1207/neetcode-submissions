# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = []
        p1 = []

        def preorder(node,stk):
            if not node:
                stk.append(None)
                return
            stk.append(node.val)
            preorder(node.left,stk)
            preorder(node.right,stk)

        p1 = []
        q1 = []

        preorder(p, p1)
        preorder(q, q1)

        return p1 == q1