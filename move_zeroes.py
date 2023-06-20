class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        n = len(nums)
        insert_pos = 0

        # Traversing the array and move non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Filling the remaining positions with zeros
        while insert_pos < n:
            nums[insert_pos] = 0
            insert_pos += 1


        
