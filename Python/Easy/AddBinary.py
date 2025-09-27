"""
(67) Add Binary
Link: https://leetcode.com/problems/add-binary/

Difficulty: Easy

Task:
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        Returns the binary string sum of 2 input binary strings.

            Parameters:
                    a (str): a string representing a binary number
                    b (str): a string representing a binary number

            Returns:
                    str: a string representing a binary number, which is the sum of a and b
        """
        
        a_int = int(a, 2)
        b_int = int(b, 2)
        total = bin(a_int + b_int)[2:]

        return total