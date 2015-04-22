"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 

Two pointers needed
p and q sets distance of n
q sets end of list boundary
Use a dummy node

Edge-ish casesL
LL length = 0
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        p = q = dummy
        for _ in range(n):
            if q != None:
                q = q.next
        if q == None or n == 0:
            return head
        else:
            while q.next:
                q = q.next
                p = p.next
            p.next = p.next.next
        return dummy.next


