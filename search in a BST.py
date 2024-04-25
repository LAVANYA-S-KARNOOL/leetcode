lass Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return
        if root.val==val:
            return root
        if val>root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
        
