"""
(14) Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Difficulty: Easy

Task:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

# note: "prefix"
#       -> refers to starting characters not sub-strings

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Returns the longest prefix between a set of given words.

            Parameters:
                    strs (List[str]): a list of words (strings)

            Returns:
                    str: a string of the common prefix between all words in strs
        """
            
        # edge case: empty list
        if not strs:
            return ""
        
        # longest prefix can only be as long as shortest word
        prefix = min(strs, key=len)

        i = 0
        while i < len(prefix):
            for word in strs:
                if word[i] != prefix[i]:
                    # truncate prefix immediately to break out of overarching while loop
                    prefix = prefix[:i]
                    break
                
            i += 1

        # edge case: no common prefix (above loop returns None currently)
        if prefix == None:
            return ""
        
        return prefix