"""
(13) Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/

Difficulty: Easy

Task:
Given a roman numeral, return it as an integer.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        Converts a roman numeral to an integer

            Parameters:
                    s (str): a string (that represents a roman numeral)

            Returns:
                    int: Integer form of s
        """

        # ditionary to store roman numeral values
        roman_nums = { "I" : 1,
                       "V" : 5,
                       "X" : 10,
                       "L" : 50,
                       "C" : 100,
                       "D" : 500,
                       "M" : 1000 }
        
        total = 0

        num_digits = len(s)
        
        for i in range(len(s)):
            curr_value = roman_nums[s[i]]
            # checks if the current numeral is smaller than the next (to account for subtraction)
            if i + 1 < len(s) and curr_value < roman_nums[s[i+1]]:
                total -= curr_value
            else:
                total += curr_value

        return total