class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def dfs_preorder(root):
            if root==None:
                return
            l.append(root.val)
            dfs_preorder(root.left)
            dfs_preorder(root.right)
        dfs_preorder(root)
        return l
        
