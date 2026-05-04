# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def geth(root):
            if not root:
                return 0

            lef = geth(root.left)
            rig = geth(root.right)

            self.dia = max(self.dia, lef + rig)
        
            return 1 + max(lef, rig)

        geth(root)

        return self.dia
        