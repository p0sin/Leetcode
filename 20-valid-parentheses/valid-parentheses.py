class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashMap = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in hashMap:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
