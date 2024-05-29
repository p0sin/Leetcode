class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D array to store the lengths of the longest common subsequence
        # Initialize all elements to 0
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # Traverse the text1 and text2 from the last character to the first character
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, add 1 to the result from the next characters
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters do not match, take the maximum of either ignoring
                    # the current character of text1 or the current character of text2
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The answer is in the top-left cell of the matrix
        return dp[0][0]