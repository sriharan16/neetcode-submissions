class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        tmp = []
        for t in tokens:
            print(t, tmp)
            if t not in operators:
                tmp.append(int(t))
            else:
                if t == "+":
                    tmp.append(tmp.pop() + tmp.pop() )
                elif t == "-":
                    a, b = tmp.pop(), tmp.pop()
                    tmp.append(b-a)
                    # tmp.append(-tmp.pop() + tmp.pop() )
                elif t == "*":
                    tmp.append(tmp.pop() * tmp.pop() )
                elif t == "/":
                    # tmp.append(tmp.pop() // tmp.pop() )
                    a, b = tmp.pop(), tmp.pop()
                    tmp.append(int(b/a))
        return tmp.pop()