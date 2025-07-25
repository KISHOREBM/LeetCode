# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def travese(root,dis,count):
    if not root:
        return
    if count not in dis:
        dis[count]=[]
    dis[count].append(root.val)
    travese(root.left,dis,count+1)
    travese(root.right,dis,count+1)
    return dis.values()
    
class Solution(object):
    def levelOrder(self, root):
        if root==None:
            return []
        return travese(root,{},0)
        