"""
(21) Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Difficulty: Easy

Task:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges 2 linked lists into 1 sorted linked list.

            Parameters:
                    list1 (Optional[ListNode]): a sorted linked list
                    list2 (Optional[ListNode]): a sorted linked list

            Returns:
                    Optional[ListNode]: a sorted linked list of list1 and list2 merged
        """
        
        # initiate dummy node to build merged list off of
        output = ListNode(0)
        tail = output

        # traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        # when one list is exhausted, append the rest of the other list
        tail.next = list1 if list1 else list2
        return output.next #ignore initial dummy node