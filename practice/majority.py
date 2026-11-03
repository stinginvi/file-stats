# 题目：找出数组中的多数元素（出现次数严格大于 n/2）。
# 要写两种解法：字典计数、摩尔投票。


def majority_count(nums: list[int]) -> int:
    """字典计数。时间 O(n)，空间 O(字符种类数)。"""
    count_map: dict[int, int] = {}
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1

    threshold = len(nums) / 2
    for num, cnt in count_map.items():
        if cnt > threshold:
            return num
    return -1  # Deleted:    dict = {}


def majority_vote(nums: list[int]) -> int:
    """摩尔投票。时间 O(n)，空间 O(1)。"""
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # 摩尔投票只保证选出"可能"的候选人，仍需二次验证是否真过半
    verified = sum(1 for x in nums if x == candidate)
    return candidate if candidate is not None and verified > len(nums) / 2 else -1


if __name__ == "__main__":
    cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 2, 1, 2, 1], 1),
    ]
    funcs = [majority_count, majority_vote]
    failed = 0
    for fn in funcs:
        print(f"--- {fn.__name__} ---")
        for nums, expect in cases:
            got = fn(nums)
            ok = got == expect
            failed += 0 if ok else 1
            print(f"{nums} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
