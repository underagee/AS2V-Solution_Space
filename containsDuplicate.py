class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
    
        for i in nums:
            if i in unique_elements:
                return True
            unique_elements.add(i)
    
        return False
