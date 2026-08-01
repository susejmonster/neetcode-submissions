class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            sortedkey = ''.join(sorted(s))
            mp[sortedkey].append(s)
        return list(mp.values())