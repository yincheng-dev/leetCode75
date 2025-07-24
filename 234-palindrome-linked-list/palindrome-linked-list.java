/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {

        if (head == null || head.next == null) return true;

        // 1. find the middle using slow and fast pointers
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next !=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        // 2. reverse the second half of the list
        ListNode secondHalf = reverseList(slow);

        // 3.compare both halves
        ListNode firstHalf = head;
        
        while(secondHalf !=null){
            if (firstHalf.val!=secondHalf.val){
                return false;

            }

            firstHalf =firstHalf.next;
            secondHalf =secondHalf.next;

        
        } 
        return true;     

    }


    private ListNode reverseList(ListNode head){
        ListNode prev = null;
        while (head != null) {
            ListNode nextTemp = head.next;
            head.next = prev;
            prev = head;
            head = nextTemp;
        }
        return prev;


    }
  }