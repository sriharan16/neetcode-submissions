class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False

        st = []

        CTO = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in CTO:
                if st and st[-1] == CTO[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return True if not st else False