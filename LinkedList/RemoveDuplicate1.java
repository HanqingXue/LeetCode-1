 /*
 Given a sorted linked list, delete all duplicates such that each element appear only once.
 Time: O(n) Space: O(n)
 https://leetcode.com/problems/remove-duplicates-from-sorted-list/
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 

Edge Cases: Empty LL
 */

 // Definition for singly-linked list.
 // public class ListNode {
 //     int val;
 //     ListNode next;
 //     ListNode(int x) { val = x; }
 // }
 //


/* ----------> THIS SOLUTION DOESNT WORK FOR EDGE CASES LIKE 1 1 1 1 1 1. Look at Cracking or HR answer <------------*/
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {  
        if(head == null) return head;  // Empty LL
        ListNode current = head;  // Current pointer
        while(current.next !=null ) { // Don't traverse down too much
            if(current.val == current.next.val) current.next = current.next.next; // Changing pointers  
            else current = current.next; // Incrementing current
            }  
        return head;  
    } 
}
