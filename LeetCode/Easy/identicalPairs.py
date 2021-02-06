class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        arrLength = len(nums)
        counter = 0
        for i in range (arrLength):
            x = i + 1
            while (x < arrLength):
                if (nums[i] == nums[x]):
                    counter += 1
                x += 1
        return counter