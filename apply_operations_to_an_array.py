class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        
        zero_count = 0
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]

        for i in range(n - zero_count, n):
            nums[i] = 0

        return nums
