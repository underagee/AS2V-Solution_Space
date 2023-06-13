class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n

        for i, num in enumerate(nums):
            missing ^= num
            missing ^= i

        return missing 
