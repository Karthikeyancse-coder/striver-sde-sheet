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
    
    def allRootToLeaf(self, root):
        res = []
    
        def dfs(node,ds):
            if node is None:
                return
        
            ds.append(node.val)
            if node.left is None and  node.right is None:
                res.append(ds[:])
            else:
                dfs(node.left,ds)
                dfs(node.right ,ds)
            ds.pop()

        dfs(root,[])    
        return res 
    

root = [1, 2, None, 4, 5,6,7,8]
tree = Solution().buildtree(root)
print(Solution().allRootToLeaf(tree))

