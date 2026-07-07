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

    def zigzagLevelOrder(self, root):
        res =[]
        def dfs(node,level):
            if node is None:
                return 
            

            if level == len(res):
                res.append([])
            if level %2 ==0:
                res[level].append(node.val)
            else:
                res[level].insert(0,node.val)

            dfs(node.left,level + 1)
            dfs(node.right,level + 1)
        
        dfs(root,0)
        return res 


p = [5, 1, 2, 8, None, None, 5, None, 4, None, None, 7 ]
q = [5, 1, 2, 8, None, None, 4, None, 5, None, None, 7 ]
tree1 = Solution().buildtree(p)
print(Solution().zigzagLevelOrder(tree1))

tree2 = Solution().buildtree(q)
print(Solution().zigzagLevelOrder(tree2))

