# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next == None:
            return head

        oddHead, odd = head, head
        evenHead, even = head.next, head.next

        while even.next != None and even.next.next != None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        if even.next != None:
            odd.next = even.next
            odd = odd.next

            even.next = None

        odd.next = evenHead
        return oddHead
        