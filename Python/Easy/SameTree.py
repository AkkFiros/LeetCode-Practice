"""
(100) Same Tree
Link: https://leetcode.com/problems/same-tree/

Difficulty: Easy

Task:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        Compares and determines if 2 given trees are the same.

            Parameters:
                    p (Optional[TreeNode]): the root of a binary tree
                    q (Optional[TreeNode]): the root of a binary tree

            Returns:
                    bool: True if p and q are the same, False otherwise.
        """
        # recursive solution
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
                    
        return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right) and p.val == q.val
        
"""
Notes:
- Iterative version can be implemented using either BFS or DFS
- Iterative BFS version:
    class Solution(object):
        def isSameTree(self, p, q):
            # iterative BFS solution
            queue = [(p, q)]

            while queue:
                curr = queue.pop(0)
                p_curr = curr[0]
                q_curr = curr[1]

                if p_curr == None and q_curr == None:
                    continue
                if p_curr == None or q_curr == None:
                    return False
                if p_curr.val != q_curr.val:
                    return False

                queue.append((p_curr.left, q_curr.left))
                queue.append((p_curr.right, q_curr.right))
        
            return True
- Iterative DFS version:
    class Solution(object):
        def isSameTree(self, p, q):
            # iterative DFS solution
            stack = [(p, q)]

            while stack:
                curr = stack.pop()
                p_curr = curr[0]
                q_curr = curr[1]

                if p_curr == None and q_curr == None:
                    continue
                if p_curr == None or q_curr == None:
                    return False
                if p_curr.val != q_curr.val:
                    return False

                stack.append((p_curr.left, q_curr.left))
                stack.append((p_curr.right, q_curr.right))
        
            return True
- Recurive, Iterative BFS and Iterative DFS all have O(n) time complexity as each node of the trees are visited once.
- Recursive has O(log n) average sapce complexity, O(n) in worst case when trees are skewed
- Iterative DFS has O(log n) average space complexity, O(n) in worst case when trees are skewed
- Iterative BFS has O(1) best space complexity when tree is skewed, O(n) worst case when tree is a complete binary tree.
"""