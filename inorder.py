class Solution:
    def __init__(self):
        self.l=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return 
        self.inorderTraversal(root.left)
        self.l.append(root.val)
        self.inorderTraversal(root.right)
        return self.l
