# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def travese(root,lis):
    if root==None:
        return []
    lis.append(root.val)
    travese(root.left,lis)
    travese(root.right,lis)
    return lis
class Solution(object):
    def preorderTraversal(self, root):
        return travese(root,[])
        
        