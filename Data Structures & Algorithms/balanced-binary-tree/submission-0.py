# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        let = self.geth(root.left)
        rit = self.geth(root.right)

        bf = abs(let - rit)

        if bf > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def geth(self, node):
        if not node:
            return 0

        lef = self.geth(node.left)
        rig = self.geth(node.right)

        return 1 + max(lef, rig)