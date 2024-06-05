class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        seen = set()

        for R in range(len(s)):
            if s[R] not in seen:
                seen.add(s[R])
                res = max(res, R - L + 1)
            else:
                while s[R] != s[L]:
                    seen.remove(s[L])
                    L += 1
                L += 1

        return res