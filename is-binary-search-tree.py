#problem link : https://www.hackerrank.com/challenges/is-binary-search-tree/problem
#time : o(n)

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root, left = float('-inf'), right = float('inf')):
    if not root :
        return True
    if left < root.data <  right :
        return check_binary_search_tree_(root.left,left,root.data)  and check_binary_search_tree_(root.right,root.data,right)
    return False
