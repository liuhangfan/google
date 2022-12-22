# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            layer = max(left, right) + 1

            if layer >= len(res):
                res.append([])
            res[layer].append(node.val)

            return layer
            
        dfs(root)

        return res
