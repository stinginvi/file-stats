# 题目：返回两个数组的交集，结果中每个元素只出现一次，顺序不限。
# 测试已写好，你只需要补 intersection 函数。


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1 & nums2)

if __name__ == "__main__":
    cases = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5, 6], []),
    ]
    failed = 0
    for nums1, nums2, expect in cases:
        got = intersection(nums1, nums2)
        got_sorted = sorted(got) if got is not None else None
        ok = got_sorted == sorted(expect)
        failed += 0 if ok else 1
        print(f"{nums1} ∩ {nums2} 期望 {sorted(expect)} 实际 {got_sorted} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
