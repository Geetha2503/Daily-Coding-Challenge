# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Check for the first and second nodes that are out of order
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev  # First violation
                self.second = node  # Second violation
            
            # Update prev to the current node
            self.prev = node
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Perform in-order traversal to find the two nodes
        inorder(root)
        
        # Swap the values of the two nodes found
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val