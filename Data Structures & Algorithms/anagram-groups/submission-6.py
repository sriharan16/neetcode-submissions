from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp = defaultdict(list)

        for s in strs:

            key = ''.join(sorted(s))
            grp[key].append(s)
        return list(grp.values())
        