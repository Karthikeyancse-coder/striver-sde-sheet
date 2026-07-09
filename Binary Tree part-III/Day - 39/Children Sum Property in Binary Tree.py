from collections import deque
from typing import Optional,List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildtree(self,val):
        if not val:
            return 
        
        root  = TreeNode(val[0])
        q = deque([root])
        i = 1
        
        while i < len(val):
            node = q.popleft()
            
            if i < len(val) and val[i] is not None:
                node.left = TreeNode(val[i])
                q.append(node.left)
            
            i+=1

            if i < len(val) and val[i] is not None:
                node.right = TreeNode(val[i])
                q.append(node.right)
            
            i+=1

        return root


    def checkChildrenSum(self, root: TreeNode) -> bool:
        # Your code goes here

        def dfs(node):
            if (node is  None):
                return True

            if node.left is None and node.right is None:
                return True  
            
            total = 0
            if node.left:
                total += node.left.val
            if node.right:
                total += node.right.val
            
            return node.val == total and  dfs(node.left) and dfs(node.right)
        
        return dfs(root)


val =   [1,4,3,5]
tree = Solution().buildtree(val)
print(Solution().checkChildrenSum(tree))

val = [10,4,6,1,3,2,4]
tree = Solution().buildtree(val)
print(Solution().checkChildrenSum   (tree))
