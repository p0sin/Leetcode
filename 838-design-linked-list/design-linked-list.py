class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        for i in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.addAtIndex(0, val)

        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        cur = self.head
        newNode = ListNode(val)

        if index <= 0:
            newNode.next = cur
            self.head = newNode
        else:
            for _ in range(index - 1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode

        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        cur = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)