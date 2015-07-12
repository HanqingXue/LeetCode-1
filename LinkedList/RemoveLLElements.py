# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # Creating dummy node
        dummy = ListNode(0);
        dummy.next = head
        
        # Creating reference pointers
        current, previous = head, dummy
        
        #Iterating through whole LL
        while (current):
            # Checking if value is the one wanting to be removed
            if current.val == val:
                previous.next = current.next
                current = current.next # ONLY increment CURRENT
            # If check fails then, increment PREV and CURRENT
            else:
                previous = current;
                current = current.next
        return dummy.next
        
