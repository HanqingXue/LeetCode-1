from ListNode import ListNode

l1_n1 = ListNode(5)
l1_n2 = ListNode(7)
l1_n3 = ListNode(9)

l1_n1.next = l1_n2
l1_n2.next = l1_n3

l2_n1 = ListNode(4)
l2_n2 = ListNode(6)
l2_n3 = ListNode(8)

l2_n1.next = l2_n2
l2_n2.next = l2_n3

def print_ll(node):
    while node != None:
        print(node, end = " ")
        node = node.next

#print_ll(l1_n1)

""" Merge algorithm; recursive """
# O(n) space; n recursive depth proportional to length of lists (SO)
def mergeTwoLists(l1, l2):
    if l1 == None: 
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2

print_ll(mergeTwoLists(l1_n1, l2_n1))
"""
Iterative Solution
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        
        c = head
        ptr1 = l1
        ptr2 = l2
        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                c.next = ptr1
                c = ptr1
                ptr1 = ptr1.next
            else:
                c.next = ptr2
                c = ptr2
                ptr2 = ptr2.next
        
        if ptr1:
            c.next = ptr1
        else:
            c.next = ptr2
        return head.next
"""
