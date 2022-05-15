# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        cur  = root
        
        def maxDepth(cur):
            if cur is None :
                return 0
            return 1+max((maxDepth(cur.left),maxDepth(cur.right)))
        x =  maxDepth(cur)
        print(x)
        
        def sumDepth(cur,x):
            
            if cur is None :
                return 0 
            
            if x == 1 :
                return cur.val
            
            return (sumDepth(cur.left,x-1)+sumDepth(cur.right,x-1))
        
        s =  sumDepth(cur,x)
        return s
