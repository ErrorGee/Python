class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
def InOrder(root):
    Inorder=[]
    Stack=[]
    if not root:
        return Inorder
    Curr=root
    while (Curr or len(Stack)!=0):
        while(Curr):
            Stack.append(Curr)
            Curr=Curr.left
        Curr=Stack.pop()
        Inorder.append(Curr.val)
        Curr=Curr.right
    return Inorder

if __name__=='__main__':
    root=NodeTree(1)
    root.right=NodeTree(2)
    #root.left=NodeTree(None)
    root.right.left=NodeTree(3)
    #root.right.right=NodeTree(None)

    print(InOrder(root))
