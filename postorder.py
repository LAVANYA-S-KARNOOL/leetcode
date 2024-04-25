class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def dfs_postorder(root):
            if root==None:
                return
            dfs_postorder(root.left)
            dfs_postorder(root.right)
            l.append(root.val)
        dfs_postorder(root)
        return l
        
