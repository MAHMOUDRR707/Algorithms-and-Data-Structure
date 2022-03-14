#link:https://leetcode.com/problems/binary-tree-postorder-traversal/
#time:o(log(n))
class Solution:
    def postorderTraversal(self, root) :
        z =[]
        def postorder(root):
            if root is None:
                 return z
            postorder(root.left)
            postorder(root.right)
            z.append(root.val)
        postorder(root)
        return z
