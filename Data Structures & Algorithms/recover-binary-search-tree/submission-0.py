# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        self.f = None
        self.s = None
        
        def inorder(root):
            if not root:
                return

            inorder(root.left)

            if self.prev and self.prev > root.val:

                if not self.f:
                    self.f = self.prev

                self.s = root

            self.prev = root

            inorder(root.right)


        inorder(root)

        if self.f and self.s:
            self.f, self.s = self.s, self.f


        