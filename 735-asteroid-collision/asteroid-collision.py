class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []
        for a in asteroids:
            if not stack or a > -1:
                stack.append(a)
            elif stack[-1] <= -1:
                stack.append(a)
            else:
                while stack[-1] > -1:
                        if abs(a) > stack[-1]:
                            stack.pop()
                            if not stack or stack[-1] <= -1:
                                stack.append(a)
                        elif abs(a) == stack[-1]:
                            stack.pop()
                            break
                        else:
                            break

        return stack