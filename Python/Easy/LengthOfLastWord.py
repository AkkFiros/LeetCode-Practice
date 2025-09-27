"""
(58) Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/

Difficulty: Easy

Task:
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Returns the length of the last word in a string.

            Parameters:
                    s (str): a string consisting of words and spaces

            Returns:
                    int: the length of the last word in s
        """
        
        list_s = s.split(" ")
        print(list_s)
        while list_s and list_s[-1] == "":
            list_s.pop(-1)

        print(list_s)

        return len(list_s[-1])
    
s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))