# LC 704 二分查找：给一个升序数组和目标值，返回下标，找不到返回 -1。
# 测试已写好，你只需要完成 search 函数。


def search(nums: list[int], target: int) -> int:
    """二分查找。时间 O(log n)，空间 O(1)。"""
    left, right = 0, len(nums) - 1
    while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

    # TODO: 循环条件、取中点、三种情况（等于 / 小了 / 大了）


if __name__ == "__main__":
    cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([], 3, -1),
    ]
    failed = 0
    for nums, target, expect in cases:
        got = search(nums, target)
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{nums} 找 {target} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
