# LC 35 搜索插入位置：升序数组里找 target，找到返回下标；找不到返回它「应该插入」的位置。
# 提示：和 704 是同一套模板，区别只在最后返回什么。
# 测试已写好，你只需要完成 search_insert 函数。


def search_insert(nums: list[int], target: int) -> int:
    """时间 O(log n)，空间 O(1)。"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 0, 0),
    ]
    failed = 0
    for nums, target, expect in cases:
        got = search_insert(nums, target)
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{nums} 插入 {target} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
