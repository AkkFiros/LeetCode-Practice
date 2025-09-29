"""
(83) Remove Duplicates from Sorted List
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Difficulty: Easy

Task:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        Returns a sorted linked-list with no duplicates.

            Parameters:
                    head (Optional[ListNode]): The head of a sorted linked list

            Returns:
                    Optional[ListNode]: head with the duplicated removed
        """
        # edge case: head has no nodes, or only has 1 node
        if head == None or head.next == None:
            return head
        
        # tracker when traversing through head
        curr = head

        while curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head