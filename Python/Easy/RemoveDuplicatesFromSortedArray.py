"""
(26) Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty: Easy

Task:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes all duplicate entries in a list of integer nums, and returns the number of unique elements in nums.

            Parameters:
                    nums (List[int]): a list of integers (non-decreasing sorted order)

            Returns:
                    int: The number of unique elements in nums
        """
        k = 0

        # 2-pointer overwrite approach
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k + 1] = nums[i + 1]
                k += 1

        return k + 1
    
"""
Notes:
- Problem can also be solved using in-place pop() method
- 2-pointer overwrite approach has O(n) time complexity as there is only 1 pass through of the list
- pop() method has (worst-case) O(n^2) time complexity as pop() traverses the list to find the element to remove, on top of while/for loop
- 2-pointer method results in more memory usage as list retains empty spots at the end
- pop() method results in less memory used as list is shortened through the use of pop()
"""