class Solution:
    def compress(self, chars):
        p, i = 0, 0

        while i < len(chars):
            currChar = chars[i]
            currOcc = 0

            while (i < len(chars)) and (chars[i] == currChar):
                i += 1
                currOcc += 1

            chars[p] = currChar
            p += 1

            if currOcc > 1:
                currOcc = str(currOcc)
                for n in currOcc:
                    chars[p] = n
                    p += 1

        return p           
            
