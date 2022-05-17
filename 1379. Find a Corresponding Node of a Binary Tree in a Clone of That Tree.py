# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def searching(original,cloned) :
            if original is not None:
                searching(original.left,cloned.left)
                if original ==  target :
                    self.ans = cloned
                searching(original.right,cloned.right)
        
        searching(original,cloned)
        return self.ans
