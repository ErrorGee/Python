# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root)!=-1
        
    def height(self,Node):
        if Node==None:
            return 0
        Left=self.height(Node.left)
        Right=self.height(Node.right)
        if Left==-1 or Right==-1 or abs(Left-Right)>1:
            return -1
        return max(Left, Right)+1
        
        
            
    
