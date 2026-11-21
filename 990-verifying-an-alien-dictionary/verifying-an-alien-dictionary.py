class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # 1. Hash map: character -> rank in alien alphabet
        alphabet = {ch: idx for idx, ch in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            found_diff = False

            # 2. Compare character by character up to the shorter word's length
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if alphabet[w1[j]] > alphabet[w2[j]]:
                        return False
                    found_diff = True
                    break  # w1[j] < w2[j], so this pair is sorted—stop comparing

            # 3. If all compared letters matched, one word is a prefix of the other;
            #    the shorter word must come first (e.g., "apple" before "app" is invalid)
            if not found_diff and len(w1) > len(w2):
                return False

        return True