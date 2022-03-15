#link:https://leetcode.com/problems/merge-two-binary-trees/
#time: o(n+m)
class Solution:
    def mergeTrees(self, root1, root2):
            if not root1  or not root2  :
                return root1 or root2
            result =  TreeNode(root1.val+root2.val)
            result.right=  self.mergeTrees(root1.right,root2.right)
            result.left = self.mergeTrees(root1.left,root2.left)
            
            return result
