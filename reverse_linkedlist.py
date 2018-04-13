# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr is not None and curr.next is not None:
            prev = curr.next
            curr.next = curr.next.next
            prev.next = head
            head = prev
        return head
