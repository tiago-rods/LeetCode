# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Usar inorder pois, sempre gera um array crescente, se isso for violado, não é uma BST
        stack = []
        node = root
        prev = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            
            if prev != None and node.val <= prev:
                return False

            prev = node.val
            node = node.right
        
        return True