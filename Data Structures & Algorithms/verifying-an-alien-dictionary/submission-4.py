class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = { char: i for i, char in enumerate(order) }

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]

                if rank[char1] > rank[char2]:
                    return False
                elif rank[char1] == rank[char2]:
                    continue
                else:
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True
            