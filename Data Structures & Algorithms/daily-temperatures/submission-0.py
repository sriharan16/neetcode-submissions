class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        st = []

        for i,t in enumerate(temperatures):
            print(i,t, st)
            if st and st[-1][0] < t:
                while st and st[-1][0] < t:
                    temp = st.pop()
                    res[temp[1]] = i - temp[1]
                    print(i, temp)
            st.append((t,i))
        return res
        