class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = {"(", "{", "["}
        closing = {")", "}", "]"}

        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing and len(stack) == 0:
                return False
            elif (i ==")" and stack[-1] == "(") or (i =="]" and stack[-1] == "[") or (i =="}" and stack[-1] == "{"):
                stack.pop(-1)
            else:
                return False

        if len(stack) > 0:
            return False
        return True