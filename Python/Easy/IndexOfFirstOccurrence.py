"""
(28) Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Difficulty: Easy

Task:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        Returns the index at which a substring occurs in a given string.

            Parameters:
                    haystack (str): a string
                    needle (str): a substring to search for in haystack

            Returns:
                    int: the index which needle first appears in haystack, or -1 if not found
        """
            
        # edge case: either haystack or needle is empty
        if not haystack or not needle:
            return 0
        
        # edge case: if needle is longer than haystack
        if len(needle) > len(haystack):
            return -1
        
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        
"""
Notes:
- using in() and index() functions is quite efficient as they are implemented in C
- sliding window approach and KMP approach also possible
- in()/index() solution is O(n + m) on average, O(n * m) in worst case
- sliding window is O(n * m)
- KMP is O(n + m)
"""