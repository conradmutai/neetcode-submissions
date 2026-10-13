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
        
        q.append(root) 

        while q:
            len_q = len(q)
            temp = [] 

            for _ in range(len_q):
                node = q.popleft()
                if node: 
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                res.append(temp)

        return res
