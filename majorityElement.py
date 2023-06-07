class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        for key,value in counter_nums.items():
            if value > (len(nums)/2):
                return key
