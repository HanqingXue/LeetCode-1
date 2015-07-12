# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    
    """ Time: O(n) Space: O(n) """
    def isPalindrome(self, head):
        if head == None:
            return True
        current = head
        value_list = []
        while (current):
            value_list.append(current.val)
            current = current.next
        value_list = value_list[::-1]
        
        idx = 0;
        # reset current
        current = head
        while (current):
            if current.val == value_list[idx]: 
                current = current.next
                idx += 1
            else:
                return False
        return True
