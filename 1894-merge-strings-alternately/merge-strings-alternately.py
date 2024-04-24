class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Check for max length
        max_len = max(len(word1), len(word2))

        merge_word = ""
        for i in range(max_len):
            if i <len(word1):
                merge_word += word1[i]

            if i < len(word2):
                merge_word += word2[i]

        return merge_word