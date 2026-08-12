from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def get_num(a):
            ans = 0
            st = 0
            sign = 1
            if a[0] == "-":
                st = 1
                sign = -1
            for c in a[st:]:
                ans *= 10
                ans += ord(c) - ord("0")
            return sign * ans

        def apply(a, op, b):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            if op == "/":
                q = abs(a) // abs(b)
                if a * b >= 0:
                    return q
                return -q

        st = []
        for t in tokens:
            if t in "+-*/":
                sec = st.pop()
                fir = st.pop()
                ans = apply(fir, t, sec)
                print(ans)
                st.append(ans)
            else:
                t = get_num(t)
                st.append(t)
        return int(st[-1])


s = Solution()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

ret = s.evalRPN(tokens)
print(ret)  # 22
print(get_num("-11"))
