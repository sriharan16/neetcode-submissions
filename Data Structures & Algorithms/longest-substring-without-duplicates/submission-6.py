class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hs = set()
        l = 0
        r = 1
        hs = {s[l]}
        ss = 1
        tss = 1
        while(r < len(s)):
            print(hs)

            if s[r] in hs:
                while(l<=r):
                    if s[l] == s[r]:
                        # hs.add(s[l])
                        l += 1
                        break
                    hs.remove(s[l])
                    l +=1
                    
                tss = r-l+1
            else:
                hs.add(s[r])
                tss += 1

            r += 1

            
            ss = max(ss, tss)
        return ss