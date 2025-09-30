"""
(100) Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/

Difficulty: Easy

Task:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        Determines if a given tree is symmetric about its root.

            Parameters:
                    root (Optional[TreeNode]): the root of a binary tree

            Returns:
                    bool: True if root is symmetric, False otherwise.
        """
        
        # recursive solution

        # helper function to compare child nodes
        def isMirror(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
    
"""
Notes:
- Iterative BFS solution:
    def isSymmetric(self, root):       
        # iterative BFS solution
        queue = [(root.left, root.right)]

        while queue:
            curr = queue.pop(0)
            left_child = curr[0]
            right_child = curr[1]

            if not left_child and not right_child:
                continue
            if not left_child or not right_child:
                return False
            if left_child.val != right_child.val:
                return False

            queue.append((left_child.left, right_child.right))
            queue.append((left_child.right, right_child.left))

        return True
- Both recursive and iterative BFS solutions have O(n) time complexity, as each node is visited once.
- Recursive solution has O(log n) space complexity on average for balanced trees, O(n) in worst case where tree is skewed.
- Iteratvie BFS solution has O(1) space complexity at best for skewed tree, O(n) in worst case for complete binary trees.
"""