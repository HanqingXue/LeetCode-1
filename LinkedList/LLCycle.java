/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 
 // Edge cases: [], [1,2] in the while loop cuz no fast.next.next
public class Solution {
    public boolean hasCycle(ListNode head) {
    if (head == null) return false; // If empty LL then no cycles
    ListNode fast = head, slow = head; // Two ref pointers, fast and slow
    while (fast != null && fast.next != null) { // Make sure fast doesn't fall off
        slow = slow.next; // slow goes by one
        fast = fast.next.next; // fast moves by two
        if (slow == fast) return true; // if they both catch up ==> CYCLE DETECTED
    }
    return false; // finished loop so no cycles
    }
}
