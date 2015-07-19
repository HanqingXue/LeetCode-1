/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 // http://www.algo-faq.com/Linked-List/Given-two-intersecting-linked-lists-find-out-their-point-of-intersection.php
 
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        
        int lenA = length(headA);
        int lenB = length(headB);
        
        ListNode ptrA = headA;
        ListNode ptrB = headB;
        
        if (lenA > lenB) {
            for (int i = 0; i < lenA-lenB; i++) ptrA = ptrA.next;
        }
        else {
            for (int j = 0; j < lenB-lenA; j++) ptrB = ptrB.next;
        }
        
        while (ptrA != null && ptrB != null) {
            if (ptrA == ptrB) return ptrA;
            else {
                ptrA = ptrA.next;
                ptrB = ptrB.next;
            }
        }
        return null;
        
    }
    
    public static int length(ListNode head) {
        ListNode current = head;
        int count = 0;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }
}
