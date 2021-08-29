#problem  link : https://www.hackerrank.com/challenges/30-binary-search-trees/problem
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

    def getHeight(self,root):
        #Write your code here
        l ,r = 0 ,0
        if root == None:
            return -1
        if root.right is not None:
            r =  self.getHeight(root.right) +1
        if root.left is not None :
            l = self.getHeight(root.left) +1 
        return max(l,r)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
