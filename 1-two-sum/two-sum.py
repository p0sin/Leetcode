class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            curNum = nums[i]
            complement = target - curNum
            if complement in hashMap:
                return [i, hashMap[complement]]
            else:
                hashMap[curNum] = i

        
        