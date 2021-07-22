# Definition for a binary tree node.
class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def PreOrderTraversal(root):
    FinalList=[]
    if not root:
        return FinalList
    Stack=[]
    Stack.append(root)
    while (Stack):
        Curr=Stack.pop()
        FinalList.append(Curr.val)
        if Curr.right:
            Stack.append(Curr.right)
        if Curr.left:
            Stack.append(Curr.left)
    return FinalList
  
if __name__=='__main__':
    root=NodeTree(1)
    root.left=NodeTree(2)
    root.right=NodeTree(3)
    root.left.left=NodeTree(4)
    root.left.right=NodeTree(5)
    root.right.left=NodeTree(6)
    root.right.right=NodeTree(7)
    print(PreOrderTraversal(root))


