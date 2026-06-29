class TimeMap:

    def __init__(self):
        self.tm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        l = self.tm.get(key, [])
        l.append((value, timestamp))
        self.tm[key] = l 
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.tm.get(key, [])

        l, r = 0, len(values) - 1

        while(l<=r):
            m = l + (r-l)//2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res




        
