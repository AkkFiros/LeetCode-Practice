"""
(69) Sqrt(x)
Link: https://leetcode.com/problems/sqrtx/

Difficulty: Easy

Task:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        Returns the non-negative square root of an integer x, rounded down to the nearest whole number.

            Parameters:
                    x (int): a non-negative integer

            Returns:
                    int: a non-negative integer
        """
        # edge case: sqrt(0) = 0, sqrt(1) = 1
        if x < 2:
            return x
        
        low = 0
        high = x

        # binary search approach
        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
    

"""
Notes:
- Binary search approach has O(log(n)) time complexity
- Incremental search approach has O(sqrt(x)) time complexity, which is worse for large values of x
- Newton's method:
    def mySqrt(self, x):
        if x == 0:
            return 0
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
- Newton's method also has O(log(n)) time complexity
"""

print(Solution.mySqrt(1, 8))