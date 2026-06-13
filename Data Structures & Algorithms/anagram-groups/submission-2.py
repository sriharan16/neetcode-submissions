from collections import defaultdict
class Solution:
    def isAnagram(self, str1: str, str2: str):
        if len(str1) != len(str2):
            return False
        counts = defaultdict(int)
        for s in str1:
            counts[s] += 1
        for s in str2:
            if counts[s] == 0:
                return False
            counts[s] -= 1
        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res = []
        while(strs):
            str1 = strs.pop()
            t_strs = strs.copy()
            grp = [str1]
            for s in strs:
                if self.isAnagram(str1, s):
                    grp.append(s)
                    t_strs.remove(s)
            res.append(grp)
            strs = t_strs
        return res
            

