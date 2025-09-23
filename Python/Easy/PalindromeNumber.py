"""
(9) Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Difficulty: Easy

Task:
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        Checks if an integer is a palindrome

            Parameters:
                    x (int): an integer

            Returns:
                    bool: True if x is a palindrome, False otherwise
        """

        # negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        # single digit numbers are palindromes
        if x < 10 and x >= 0:
            return True
        
        # to avoid converting x into a string, x is split and compared
        # second half of x is reversed and compared with first half
        reverse = 0

        # loop stops when reverse has more digits than forwards
        # or when forwards is a single digit (for cases where x is 2 digits)
        while x > reverse:
            last_digit = x % 10            
            reverse = reverse * 10 + last_digit
            x = x // 10

        # 2 cases:
        # forwards == reverse when x has even number of digits
        # forwards == reverse // 10 when x has odd number of digits (checks after middle digit is moved to reverse)
        return (x == reverse) or (x == reverse // 10)
             
    
"""
Notes: 

- Comparison between string conversion and half-reversal methods:
    -> String conversion:
        - Time complexity: O(log n) => no. of digits in x
        - Space constraint: O(log n) => for storing strings
    -> half-reversal:
        - Time complexity: O(log n) => no. of digits in x
        - Space constraint: O(1) => no additional space needed

    -> Analysis:
        - python's built-in string handling is highly optimized, so for smaller scales, string conversion is faster
        - for larger scales, half-reversal is better due to lower space constraint and better scalability
"""