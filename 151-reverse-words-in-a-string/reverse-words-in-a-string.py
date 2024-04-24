class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Loop through the string and make a list, eliminating all " ".
        words = []
        current_word = ""

        for c in s:
            if c != " ":
                current_word += c
            else:
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
                else:
                    continue
                    
        if current_word != "":
            words.append(current_word)

        i, j = 0, -1

        while i < (len(words) / 2):
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

            i += 1
            j -= 1

    
        return " ".join(words)
        