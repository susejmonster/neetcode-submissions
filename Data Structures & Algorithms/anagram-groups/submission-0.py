class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashing function
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))  # hashable
            groups[key].append(word)

        return list(groups.values())