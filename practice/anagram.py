# 题目：两个字符串 s 和 t，判断 t 是不是 s 的字母异位词（字母种类和个数完全一致，顺序无所谓）。
# 三种解法：排序、数组计数、字典计数。


def is_anagram_sort(s: str, t: str) -> bool:
    """排序后比较。时间 O(n log n)，空间 O(n)。"""
    return sorted(s) == sorted(t)


def is_anagram_count_list(s: str, t: str) -> bool:
    """长度 26 的数组计数。前提：字符串只含 a–z 小写字母。时间 O(n)，空间 O(1)。"""
    if len(s) != len(t):
        return False
    s_count = [0] * 26
    t_count = [0] * 26
    for ch in s:
        s_count[ord(ch) - ord("a")] += 1
    for ch in t:
        t_count[ord(ch) - ord("a")] += 1
    return s_count == t_count


def is_anagram_count_dict(s: str, t: str) -> bool:
    """一个字典加一减一。支持任意字符。时间 O(n)，空间 O(字符种类数)。"""
    if len(s) != len(t):
        return False
    diff = {}
    for ch in s:
        diff[ch] = diff.get(ch, 0) + 1
    for ch in t:
        diff[ch] = diff.get(ch, 0) - 1
        if diff[ch] < 0:
            return False
    return all(v == 0 for v in diff.values())


if __name__ == "__main__":
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("ab", "a", False),
        ("", "", True),
        ("a b", "ab", False),
    ]
    funcs = [is_anagram_sort, is_anagram_count_list, is_anagram_count_dict]
    failed = 0
    for fn in funcs:
        print(f"--- {fn.__name__} ---")
        for s, t, expect in cases:
            got = fn(s, t)
            ok = got == expect
            failed += 0 if ok else 1
            print(f"{s!r:10} {t!r:10} 期望 {str(expect):5} 实际 {str(got):5} {'OK' if ok else 'FAIL'}")

    # 数组版只认小写字母的实证：取消注释会抛 IndexError
    # print(is_anagram_count_list("Ab", "bA"))

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
