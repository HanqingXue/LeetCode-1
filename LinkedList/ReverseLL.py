# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

""" Iterative Solution """
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        current = head
        previous = None
        temp = head
        
        while current: # while current != None:
            temp = current.next
            current.next = previous
            
            previous = current
            current = temp
        return previous
