"""
(88) Remove Duplicates from Sorted List
Link: https://leetcode.com/problems/merge-sorted-array/

Difficulty: Easy

Task:
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order,
and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merges 2 sorted integers arrays into 1 sorted integer array.

            Parameters:
                    nums1 (List[int]): an integer array
                    m (int): the number of elements in nums1 to be merged
                    nums2: (List[int]): an integer array
                    n (int): the number of elements in nums2 to be merged

            Returns:
                    List[int]: nums1 after merging with nums2
        """
        
        # edge cases: either m or n is 0
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1
        if n == 0:
            return nums1
        
        ptr_main = m + n - 1
        ptr1 = m - 1
        ptr2 = n - 1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr_main] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr_main] = nums2[ptr2]
                ptr2 -= 1
            ptr_main -= 1

        while ptr2 >= 0:
            nums1[ptr_main] = nums2[ptr2]
            ptr2 -= 1
            ptr_main -= 1

        return nums1