"""
(1) Two Sum
Link: https://leetcode.com/problems/two-sum/

Difficulty: Easy

Task:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# note: "each input would have exactly one solution"
#       -> can return first valid pair
#       -> guaranteed to have a solution, no negative case handling needed

# note: adding a number to hashmap before finding complement leads to errors when there are duplicate entries
#       -> indinces are not selected properly

class Solution(object):
    def twoSum(self, nums, target):
        """
        Returns the indices of two integers within nums which sum equates to target.

            Parameters:
                    nums (List[int]): a list of integers
                    target (int): a integer

            Returns:
                    List<int>: a list containing a pair of indices (integers), whose corresponding values add up to the target
        """
        # use a hash map to store the indices of numbers for O(n) runtime
        # looking through the list each time results in O(n^2)
        hash_map = {}

        for i, digit in enumerate(nums):

            # find the complement that adds up to target with current number
            complement = target - digit

            # if complement is already in the hash map, return the indices
            # (index of complement is stored in hashmap)
            if complement in hash_map:
                return [hash_map[complement], i]
            
            # store index of current number for future complement lookup
            hash_map[digit] = i