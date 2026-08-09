class Solution:
    def calculate(self, s: str) -> int:
        # self eval
        def _eval(n):
            ints = list(map(lambda x: ord(x) - ord("0"), n))
            ans = 0
            for i in ints:
                ans *= 10
                ans += i
            return ans

        # cut operators
        s = s.replace(" ", "")
        if s[0] == "-":
            s = "0" + s
        N = len(s)
        infix = []
        # L = R = 0
        # while R < N:
        #     if s[R] in "+-*/()":
        #         infix.append(s[R])
        #         R += 1
        #         L = R
        #     else:
        #         while R < N - 1 and s[R + 1] not in "+-*/()":
        #             R += 1
        #         infix.append(_eval(s[L : R + 1]))
        #         R += 1
        #         L = R
        def is_num_str(st):
            return ord("0")<=ord(st)<=ord("9")
        cur=0
        nxt=1
        while nxt<N:
            if is_num_str(s[cur]):
                

        print(infix)
        # infix to suffix
        op_order = {"+": 0, "-": 0, "*": 1, "/": 1}

        def compare_op(op_0, op_1):
            return op_order[op_0] - op_order[op_1]

        def is_numeric(op):
            return isinstance(op, int)

        stack = []
        suffix = []
        for ele in infix:
            if is_numeric(ele):
                suffix.append(ele)
                continue
            if ele == "(":
                stack.append(ele)
                continue
            elif ele == ")":
                while stack[-1] != "(":
                    suffix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != "(" and compare_op(ele, stack[-1]) <= 0:
                    suffix.append(stack.pop())
                stack.append(ele)
        while stack:
            suffix.append(stack.pop())

        # cal suffix
        def perform_op(ele_0, ele_1, op):
            if op == "+":
                return ele_0 + ele_1
            if op == "-":
                return ele_0 - ele_1
            if op == "*":
                return ele_0 * ele_1
            if op == "/":
                return ele_0 / ele_1

        for ele in suffix:
            if is_numeric(ele):
                stack.append(ele)
            else:
                ele_1 = stack.pop()
                ele_0 = stack.pop()
                ret = perform_op(ele_0, ele_1, ele)
                stack.append(ret)
        return stack[-1]


print(Solution().calculate(s="1 + 1"), 2)
print(Solution().calculate(s="2-1 + 2"), 3)
print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)"), 23)
print(Solution().calculate(s="-(10+(4+5+2)-3)+(6+8)"), eval("-(10+(4+5+2)-3)+(6+8)"))
print(Solution().calculate(s="9+(3-1)*3+10/2"), eval("9+(3-1)*3+10/2"))
