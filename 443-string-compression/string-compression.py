class Solution:
    def compress(self, chars):
        r, i = 0, 0

        while(i < len(chars)):
            currChar = chars[i]
            currOcc = 0
            while ((i < len(chars)) and (chars[i] == currChar)):
                currOcc += 1
                i += 1

            chars[r] = currChar
            r += 1
            if(currOcc > 1):
                currOccStr = str(currOcc)
                for j in range(len(currOccStr)):
                    chars[r] = currOccStr[j]
                    r += 1

        return r            
            
