/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode previous = null;
        ListNode temp = current;
        
        while (current != null) {
            temp = current.next;
            current.next = previous;
            
            previous = current;
            current = temp;
        }
        return previous;
    }
}
