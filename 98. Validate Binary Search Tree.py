# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
     def validation(root,min_v,max_v):
        if root is None :
            return 1   
        if (min_v >=  root.val) or (max_v <=  root.val):
            return 0 
        
        return (validation(root.left,min_v,root.val) and  validation(root.right,root.val,max_v))
     return validation(root,-2**32,2**31)

        

