# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
#  Using hare and tortoise method for finding middle node in LL

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Storing head into temp variable
        temp = head
        # assigning slow pointer at temp(head)
        slow = temp
        # assigning fast pointer at temp(head)
        fast = temp
        # Checking for the end node i.e. null 
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        # returning the slow pointer or returning second half of linked list
        return slow