"""
(94) Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Difficulty: Easy

Task:
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        Traverses a given Binary Tree in order.

            Parameters:
                    root (Optional[TreeNode]): a binary tree

            Returns:
                    List[int]: the value of nodes in root with inorder traversal arrangement
        """
        # recursive solution
        
        # base case
        if root == None:
            return []
        
        return Solution.inorderTraversal(self, root.left) + [root.val] + Solution.inorderTraversal(self, root.right)
    
"""
Notes:
- Iterative version:
    class Solution(object):
        def inorderTraversal(self, root):
            # iterative solution
            curr = root
            stack = []
            result = []

            # base case
            if root == None:
                return result

            while stack or curr != None:
                if curr == None:
                    this = stack.pop()
                    result.append(this.val)
                    curr = this.right
                else:
                    stack.append(curr)
                    curr = curr.left

            return result
- both recursive and interative solutions have O(n) time complexity as each node is visited once
- both recursive and iterative solutions have O(h + log n) space complexity for best-case balanced tree,
  O(h + n) for worst-case skewed tree
"""