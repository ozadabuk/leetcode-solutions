# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q = deque([])
        carry = 0
        head = ListNode()
        curr = head
        while (l1 is not None) or (l2 is not None):
            n1=0
            n2=0
            val = 0
            if l1 is not None:
                n1 = l1.val
                l1 = l1.next
            if l2 is not None:
                n2 = l2.val
                l2 = l2.next
            tsum = n1 + n2 + carry
            val = tsum % 10
            carry = 1 if tsum > 9 else 0
            curr.val = val
            if (l1 is not None or l2 is not None):
                curr.next = ListNode()
                curr = curr.next
            elif carry != 0:
                curr.next = ListNode(carry)
                curr = curr.next
        return head