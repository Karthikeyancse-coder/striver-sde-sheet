from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildtree(self, values):
        if not values:
            return None

        root = TreeNode(values[0])
        q = deque([root])
        i = 1

        while q and i < len(values):
            node = q.popleft()

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1

        return root

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left)and self.isSameTree(p.right, q.right))


# Driver code
sol = Solution()

p = [5, 1, 2, 8, None, None, 5, None, 4, None, None, 7 ]
q = [5, 1, 2, 8, None, None, 4, None, 5, None, None, 7 ]
tree1 = sol.buildtree(p)
tree2 = sol.buildtree(q)

result = sol.isSameTree(tree1, tree2)

print(result)
