# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        node = ListNode(next = l3) 
        carryOver = 0

        # until both lists are over
        while l1 != None or l2 != None:
            node = node.next

            #if one of the lists is over
            if l1 == None:
                value = l2.val + carryOver
                l2 = l2.next
            elif l2 == None:
                value = l1.val + carryOver
                l1 = l1.next
            
            #if no list is over
            else:
                value = l1.val + l2.val + carryOver
                l1 = l1.next
                l2 = l2.next
            
            node.val = value % 10
            carryOver = value // 10 

            node.next = ListNode()

        if carryOver != 0:
            node = node.next
            node.val = 1
            node.next = ListNode()
        
        node.next = None

        return l3