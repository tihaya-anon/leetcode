infix = [9, "+", "(", 3, "-", 1, ")", "*", 3, "+", 10, "/", 2]
print(" ".join(map(str, infix)))


def cal(infix):
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


ret = cal(infix)
print(ret)
