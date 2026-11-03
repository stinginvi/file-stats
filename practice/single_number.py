# 题目：除了某个元素只出现一次以外，其余元素都出现两次。找出那个只出现一次的元素。
# 要求：时间 O(n)，空间 O(1)。


def single_number(nums: list[int]) -> int:
    """用异或消掉成对出现的数。"""
    result = 0
    for n in nums:
        result ^= n
    return result


if __name__ == "__main__":
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([0, 1, 0], 1),
    ]
    failed = 0
    for nums, expect in cases:
        got = single_number(nums)
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{nums} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
