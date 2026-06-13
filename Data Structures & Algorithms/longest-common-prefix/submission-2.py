class Solution:

    def get_common_prefix(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1
        prefix = ""
        for i in range(len(min(str1,str2))):
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        l_prefix = strs[0]
        if n == 1:
            return l_prefix
        for i in range(1,n):
            l_prefix = self.get_common_prefix(l_prefix, strs[i])
            if l_prefix == "":
                return l_prefix

        return l_prefix