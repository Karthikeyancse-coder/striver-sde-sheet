from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inMap  ={ val: i for i,val in  enumerate(inorder)}
        idx = len(postorder) -1

        def dfs(left,right):
            nonlocal idx 
            if left > right:
                return None
            
            rootVal = postorder[idx]
            idx -= 1

            root = TreeNode(rootVal)
            mid = inMap[rootVal]

            root.right = dfs(mid+1,right)
            root.left = dfs(left,mid-1)

            return root

        return dfs(0,len(inorder)-1)

    
postorder = [9, 15, 7, 20, 3]
inorder = [9,3,15,20,7]
print(Solution().buildTree(inorder,postorder))
