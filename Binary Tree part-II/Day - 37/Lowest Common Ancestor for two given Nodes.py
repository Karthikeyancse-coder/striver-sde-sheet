from collections import deque

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

    def find(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return root

        left = self.find(root.left, val)
        if left:
            return left

        return self.find(root.right, val)

    def lowestCommonAncestor(self, root, p, q):

        def dfs(node):
            if node is None:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right

        return dfs(root)


sol = Solution()

root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
tree = sol.buildtree(root)

p = sol.find(tree, 5)
q = sol.find(tree, 1)

lca = sol.lowestCommonAncestor(tree, p, q)

print("Lowest Common Ancestor:", lca.val)
