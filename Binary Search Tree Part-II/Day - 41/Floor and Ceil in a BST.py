from collections import deque
from typing import Optional,List 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def Insert(self,root,val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.Insert(root.left,val)

        else: 
            root.right = self.Insert(root.right,val)

        return root 


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for val in preorder:
            root = self.Insert(root,val)

        return root 
    
    def floorCeilOfBST(self, root, key):
        ceil = floor = -1
        def dfs(node):
            nonlocal floor, ceil
            if node is None:

                return
            if key == node.val:
                floor = ceil = node.val
                return
                 
            
            if key > node.val:
                floor = node.val
                dfs(node.right)
            
            else:
                ceil = node.val 
                dfs(node.left)
        dfs(root)

        return [floor, ceil]


                    

    

val = [8, 4, 12, 2, 6, 10, 14]
key = 11
tree = Solution().bstFromPreorder(val)
print(Solution().floorCeilOfBST(tree,key))

val = [8, 4, 12, 2, 6, 10, 14]
key = 15
tree = Solution().bstFromPreorder(val)
print(Solution().floorCeilOfBST(tree,key))
