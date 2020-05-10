class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None ,p,q):
            return root 
        L = self.lowestCommonAncestor(root.left,p,q)
        R =self.lowestCommonAncestor(root.right,p,q)
        return R if None==L else L if None==R else root