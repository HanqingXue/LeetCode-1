/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode boundary = dummy;
        ListNode current = dummy;
        
        for (int i = 0; i < n; i++) {
            boundary = boundary.next;
        }
        
        while (boundary.next != null) {
            boundary = boundary.next;
            current = current.next;
        }
        current.next = current.next.next;
        return dummy.next;
    }
}
