# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        
        if root:
            q.append(root) 

        while q:
            len_q = len(q)
            temp = [] 

            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)
                l, r = node.left, node.right

                if l:
                    q.append(l)
                if r: 
                    q.append(r)

            res.append(temp)

        return res
