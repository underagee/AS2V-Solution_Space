class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        init_index = 0
        final_index = len(s) - 1
    
        while init_index < final_index:
            s[init_index], s[final_index] = s[final_index], s[init_index]
            init_index += 1
            final_index -= 1
