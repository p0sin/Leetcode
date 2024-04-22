class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        for letter in t:
            if letter not in letters:
                return False
            else:
                letters[letter] -= 1
                if letters[letter] == 0:
                    letters.pop(letter)
        if len(letters) > 0:
            return False
        return True

        