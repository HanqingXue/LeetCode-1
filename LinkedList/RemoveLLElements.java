/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0); // Create a Dummy node
        dummy.next = head; // Set dummy's next to head;
        
        ListNode current = head, previous = dummy; // Two ref pointers; prev using dummy
        while (current != null) { // iterate through whole lLL
            // Don't increment previous here
            if (current.val == val) {  // If val wanted to be removed
                previous.next = current.next; // Rewiring pointers
                current = current.next; // Incrementing current ONLY
            }
            // If not = to val wanted to be removed then increment prev and current pointers
            else {
            previous = current;
            current = current.next;
            }
        }
        return dummy.next;
    }
}
