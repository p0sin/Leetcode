# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeLinks(lists):
            if len(lists) == 0:
                return
            if len(lists) == 1:
                return lists[0]

            midIndex = len(lists) // 2
            left = mergeLinks(lists[midIndex:])
            right = mergeLinks(lists[:midIndex])

            return merge(left, right)


        def merge(list1, list2):
            dummy = tail = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if not list1:
                tail.next = list2
            else:
                tail.next = list1

            return dummy.next

        return mergeLinks(lists)
        


        