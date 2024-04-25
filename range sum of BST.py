class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l=[]
        res=0
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for i in l :
            if (low <= i <= high) :
                res += i
        return res 





