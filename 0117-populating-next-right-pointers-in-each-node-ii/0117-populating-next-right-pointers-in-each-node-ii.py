class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        from collections import deque
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root