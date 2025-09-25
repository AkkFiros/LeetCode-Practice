"""
(20) Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy

Task:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        Checks if s is valid.

            Parameters:
                    s (List[str]): a list of parentheses (string)

            Returns:
                    bool: returns True if s is valid. False otherwise
        """
        
        # edge case: s is empty
        if not s:
            return True
        
        # LIFO stack to track parentheses and their order
        stack = []

        maps = { ")" : "(",
                 "]" : "[",
                 "}" : "{" }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                if maps[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False    
        return not stack
    
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"

print(Solution.isValid(1, s1))
print(Solution.isValid(1, s2))
print(Solution.isValid(1, s3))
print(Solution.isValid(1, s4))
print(Solution.isValid(1, s5))