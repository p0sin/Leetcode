class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv}

        stack = []
        
        for t in tokens:
            try:
                num = int(t)
                stack.append(num)
            except ValueError:
                a = stack.pop()
                b = stack.pop()
                operation = operations[t](b, a)
                stack.append(int(operation))
            
        return stack[0]