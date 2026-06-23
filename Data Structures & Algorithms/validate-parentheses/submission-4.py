from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        l = deque()

        for c in s:
            if c in ['(', '[', '{']:
                l.append(c)
            if c in [')', ']', '}']:
                if not l:
                    return False
                cc = l.pop()
                if not ((c == ')' and cc == '(') or (c == ']' and cc == '[') or (c == '}' and cc == '{')):
                    return False

        return False if l else True


