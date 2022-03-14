#link:https://leetcode.com/problems/binary-tree-inorder-traversal/
#time:o(log(n))
class Solution:
    def inorderTraversal(self, root) -> List[int]:
        z =[]
        def inorder(root):
            if root is None :
                return z 
            inorder(root.left)
            z.append(root.val)
            inorder(root.right)
        inorder(root)
        return z
