"""
(70) Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

Difficulty: Easy

Task:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# note: Fibonacci Sequence question

class Solution(object):
    def climbStairs(self, n):
        """
        Returns the number of distinct ways to climb to the top of a staircase.

            Parameters:
                    n (int): an integer between 1 and 45, inclusive

            Returns:
                    int: the number of distinct ways to climb a staircase with n steps
        """
        # base cases: when n = 1, number of ways = 1; when n = 2, number of ways = 2
        if n <= 2:
            return n
        
        n1, n2 = 1, 2

        for i in range(3, n + 1):
            n1, n2 = n2, n1 + n2

        return n2