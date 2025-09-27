"""
(66) Plus One
Link: https://leetcode.com/problems/plus-one/

Difficulty: Easy

Task:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        Returns a large integer that is an increment of 1 of the input.

            Parameters:
                    digits (List[int]): a list of integers representing a large integer

            Returns:
                    List[int]: a list of integers representing a large integer
        """
        
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            len_digits = len(digits)
            carry_over = 1
            curr_digit = len_digits - 2
            
            # while loop to handle addition of carry_over to digits
            # loop runs while there is a carry_over and digits has not been fully traversed
            while carry_over and curr_digit >= 0:
                if digits[curr_digit] == 9:
                    digits[curr_digit] = 0
                    curr_digit -= 1
                    continue
                else:
                    digits[curr_digit] += 1
                    return digits
            
            # if loops does not handle carry_over, additional '1' needs to be added in front
            digits[0] = 0
            digits.insert(0, 1)

        return digits