class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Create a dictionary that each key is a list of how much each letter is repeated
        anagrams = defaultdict(list)

        for word in strs:
            # Create a list that counts each time a letter is seen
            letters_repeated = [0] * 26 # a...z
            
            for letter in word:
                letters_repeated[ord(letter) - ord("a")] += 1

            anagrams[tuple(letters_repeated)].append(word)
        
        return anagrams.values()


        