/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
 // Iterative Solution
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Create a new dummy head
        ListNode head = new ListNode(0);
        
        /* Creating ref pointers */
        ListNode c = head; // head pointer 
        ListNode ptr1 = l1; 
        ListNode ptr2 = l2;
        
        /* Rewiring the pointers in while loop */
        while ((ptr1 != null) && (ptr2 != null)) {  // Iterate until one lists ends
            if (ptr1.val <= ptr2.val)  { // l1.val <= l2.val
                c.next = ptr1; // next in head pointer; take smaller one (l1)
                c = ptr1; // increment head pointer
                ptr1 = ptr1.next; // increment list pointer
            } 
            else { // l1.val < l2.val
            c.next = ptr2; // next in head pointer; take larger (l2)
            c = ptr2; // increment 
            ptr2 = ptr2.next;
            } 
        }
        
        /* Check whichever one is ended outside loop and append to LL*/
        if (ptr1 == null) c.next = ptr2;
        else c.next = ptr1;
        //c.next = (ptr1 == null) ? ptr2 : ptr1; 
        return head.next; 
    } 
    
}
