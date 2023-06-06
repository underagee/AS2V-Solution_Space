class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {c: i for i, c in enumerate(order)}
    
        for i in range(1, len(words)):
            past_word = words[i - 1]
            present_word = words[i]
            
            for j in range(min(len(past_word), len(present_word))):
                if past_word[j] != present_word[j]:
                    if alien_dict[past_word[j]] > alien_dict[present_word[j]]:
                        return False
                    break
            else:
                if len(past_word) > len(present_word) and present_word[:len(past_word)] == present_word:
                    return False
            return True
