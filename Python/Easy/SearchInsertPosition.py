"""
(35) Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/

Difficulty: Easy

Task:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

# note: cannot use in() / index() as they are O(n), solution requires O(log n)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        Returns the index at which a substring occurs in a given string.

            Parameters:
                    nums (List[int]): a sorted list of distinct integers
                    target (int): an integer to search in/insert into nums

            Returns:
                    int: the index that target is found in nums, or where it would be inserted
        """
             
        # binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left