class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        vowel_count = 0

        # Initial count of vowels in the first `k` characters
        for i in range(k):
            if s[i] in vowels_set:
                vowel_count += 1

        # Set the initial max_vowels to vowel_count
        max_vowels = vowel_count

        # Use a sliding window to count vowels in the rest of the string
        for i in range(1, len(s) - k + 1):
            # Subtract the vowel if the previous window's first char is a vowel
            if s[i - 1] in vowels_set:
                vowel_count -= 1
            # Add the vowel if the new window's last char is a vowel
            if s[i + k - 1] in vowels_set:
                vowel_count += 1
            # Update max_vowels with the maximum seen so far
            max_vowels = max(max_vowels, vowel_count)

        return max_vowels


        