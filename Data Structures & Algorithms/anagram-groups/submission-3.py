from collections import defaultdict

class Solution:
    def isAnagram(self, str1: str, str2: str)-> bool:
        if len(str1) != len(str2):
            return False
        d = defaultdict(int)
        for s in str1:
            d[s] += 1
        
        for s in str2:
            if d[s] == 0:
                return False
            d[s] -= 1

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []
        if len(strs) == 1:
            return [strs]
        group_anagrams = [[strs[0]]]

        for i in range(1,len(strs)):
            f = False
            for group in group_anagrams:
                if self.isAnagram(strs[i], group[0]):
                    f = True
                    group.append(strs[i])
                    break
            if not f:
                group_anagrams.append([strs[i]])
        return group_anagrams



    
        