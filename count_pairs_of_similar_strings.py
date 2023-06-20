class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def is_similar(word1, word2):
            # Checking if word1 and word2 are similar
            return set(word1) == set(word2)

        similar_pairs = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_similar(words[i], words[j]):
                    similar_pairs += 1

        return similar_pairs
