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
    
    def levelOrder(self, root):
        res = {}  
        
        def dfs(node,level):
            if node is  None:
                return 
            if level  not in  res:
                res[level] = []
            res[level].append(node.val)
            dfs(node.left,level +1 )
            dfs(node.right,level +1)
        dfs(root,0)
        return [res[x]  for x in sorted(res)]
            
         

root = [1, 2, None, 4, 5,6,7,8]
tree = Solution().buildtree(root)
print(Solution().levelOrder(tree))

