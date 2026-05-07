# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        
        depthCounter = 0
        queue = deque([root])

        while queue:
            depthCounter += 1   
            levelSize = len(queue)
            for _ in range(levelSize):
                leaf = queue.popleft()
            
                if leaf.left:
                    queue.append(leaf.left)
                if leaf.right:
                    queue.append(leaf.right)
            

        return depthCounter