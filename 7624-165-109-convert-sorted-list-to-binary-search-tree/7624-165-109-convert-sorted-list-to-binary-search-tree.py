class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head
        slow_prev = None

        # Find the middle node (slow pointer)
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        # Create root node from the middle element
        root = TreeNode(slow.val)

        # Disconnect the left half from the middle
        slow_prev.next = None

        # Recursively construct left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root