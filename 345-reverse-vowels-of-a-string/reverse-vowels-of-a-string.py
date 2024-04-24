class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = {'a', 'e', 'i', 'o', 'u'}

        hold = []

        for letter in s:
            if letter.lower() in vowels:
                hold.append(letter)

        reverse = -1

        res = list(s)

        for i in range(len(s)):
            if res[i].lower() in vowels:
                res[i] = hold[reverse]
                reverse -= 1
        
        return "".join(res)
                
