#link:https://leetcode.com/problems/binary-tree-preorder-traversal/
#time:o(log(n))
class Solution:
    def preorderTraversal(self, root):
        z = []
        def xxx(root):
            if root is None :
                return z
            z.append(root.val)
            xxx(root.left)
            xxx(root.right)
            
            
        xxx(root)    
        return z
