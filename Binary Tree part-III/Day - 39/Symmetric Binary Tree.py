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



    def is_symmetric(self, root):
        #your code goes here
         
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            return dfs(left.left,right.right) and dfs(right.right,left.left)
        
        if not root:
            return True
        
        return dfs(root.left,root.right)


val =  [1, 2, 2, 3, 4, 4, 3]
tree = Solution().buildtree(val)
print(Solution().is_symmetric(tree))

val = [1, 2, 2, None, 3, None, 3]
tree = Solution().buildtree(val)
print(Solution().is_symmetric(tree))

