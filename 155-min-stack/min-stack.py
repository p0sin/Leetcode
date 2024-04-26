class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val < self.min_stack[-1] or val == self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min_stack[-1]:
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()   
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()