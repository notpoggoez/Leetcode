# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new = slow.next 
        slow.next = None 

        prev = None 
        while new:
            temp = new.next
            new.next = prev
            prev = new 
            new = temp
        
        while prev:
            temp2 = head.next 
            head.next = prev
            prev = prev.next 
            head.next.next = temp2
            head = head.next.next