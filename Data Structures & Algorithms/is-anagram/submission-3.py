from collections import Counter, defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for c in t:
            if counts[c] == 0:
                return False
            counts[c] -= 1
        return True
        
        