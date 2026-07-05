from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildtree(self,value):
        if not value:
            return None
        root = TreeNode(value[0])
        q = deque([root])
        i = 1 
        while q and i < len(value):
            node = q.popleft()
            
            if i < len(value) and value[i] is not None:
                node.left = TreeNode(value[i])
                q.append(node.left)
            i+=1
            if i < len(value) and value[i] is not None:
                node.right = TreeNode(value[i])
                q.append(node.right)
            i+=1
        return root 
    
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        #your code goes here
        first = {}
        ans = [0]

        def dfs(node,level,idx):
            if node is None:
                return
            
            if level not in first:
                first[level] = idx

            ans[0] = max(ans[0], idx - first[level] + 1 )
            dfs(node.left, level + 1 , idx * 2 )
            dfs(node.right, level + 1 , idx * 2 + 1)

        dfs(root , 0,0 )
        return ans[0]
         

root = [1, 2, None, 4, 5,6,7,8]
tree = Solution().buildtree(root)
print(Solution().widthOfBinaryTree(tree))

