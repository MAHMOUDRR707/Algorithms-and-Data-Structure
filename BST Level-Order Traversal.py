#problem link : https://www.hackerrank.com/challenges/30-binary-trees/problem
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
     if root:
        z = [root]
        while z :
            x  = z.pop()
            print(x.data,end =' ')
            if x.left :
                z.insert(0,x.left)
            if x.right :
                z.insert(0,x.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
