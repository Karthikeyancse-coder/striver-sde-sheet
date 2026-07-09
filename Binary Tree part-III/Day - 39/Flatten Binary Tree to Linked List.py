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


    def flatten(self, root: Optional[TreeNode]) -> None:
            curr  = root

            while curr is not None:
                if curr.left:
                    preV = curr.left
                    while preV.right:
                        preV = preV.right
    
                    preV.right = curr.right
                    curr.right = curr.left
                    curr.left = None
    
                curr = curr.right 
    
            return root


val =  [1, 2, 2, 3, 4, 4, 3]
tree = Solution().buildtree(val)
print(Solution().flatten(tree))

val = [1, 2, 2, None, 3, None, 3]
tree = Solution().buildtree(val)
print(Solution().flatten(tree))
