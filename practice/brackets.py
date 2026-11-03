def is_valid(s: str) -> bool:
    """判断括号串是否合法"""
    stack = []
    # 右括号 → 对应左括号 的映射表
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":                 # 左括号：压栈记账
            stack.append(ch)
        elif ch in pairs:               # 右括号：查账
            if not stack or stack[-1] != pairs[ch]:
                return False            # 没得配 or 配不上 → 非法
            stack.pop()                 # 配成功，销账
        # 其他字符题目里没有，忽略即可
    return not stack                    # 栈清空了才算全部配对


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        ("", True),
    ]
    for s, expect in tests:
        got = is_valid(s)
        print(f"{s!r:10} 期望 {expect} 实际 {got} {'OK' if got == expect else 'FAIL'}")