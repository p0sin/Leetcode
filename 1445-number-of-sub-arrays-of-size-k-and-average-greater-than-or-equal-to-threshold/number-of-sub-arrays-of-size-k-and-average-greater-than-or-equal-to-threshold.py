class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, R = 0, k -1
        res = 0
        totalSum = sum(arr[L : R + 1])

        while R < len(arr):
            avg = totalSum / k

            if avg >= threshold:
                res += 1

            totalSum -= arr[L]
            L += 1

            R += 1
            if R < len(arr):
                totalSum += arr[R]

        return res