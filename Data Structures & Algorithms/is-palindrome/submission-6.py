class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "")
        i = 0
        j = len(s) - 1
        while i<j:
            # while i<j and not self.alphaNum(s[i]):
            while i<j and not s[i].isalnum():
                i +=1
            while i<j and not self.alphaNum(s[j]):
                j -=1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))