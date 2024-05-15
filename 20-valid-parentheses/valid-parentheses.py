class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            
            else:
                if not stack:
                    return False
                elif b == ")" and stack[-1] != "(":
                    return False
                elif b == "]" and stack[-1] != "[":
                    return False
                elif b == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        if stack:
            return False
        return True

        