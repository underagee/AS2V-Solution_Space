class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs, key=len)
    
        for i, ch in enumerate(shortest):
            for other in strs:
                if shortest[i] != other[i]:
                    return shortest[:i]
    
        return shortest 
