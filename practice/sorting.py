# 手写两种排序，和 Python 自带的 sorted 对比结果。
# 要求：返回新列表，不要修改传入的列表。


def insertion_sort(nums: list[int]) -> list[int]:
    """插入排序：像整理扑克牌，把每张牌插到前面已排好的合适位置。时间 O(n^2)。"""
    arr = list(nums)  # 复制一份，不动原列表
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(nums: list[int]) -> list[int]:
    """冒泡排序：相邻两个比大小，大的往后冒。时间 O(n^2)。"""
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    cases = [
        [5, 2, 9, 1],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [],
        [7],
        [3, 3, 1, 3],
    ]
    funcs = [insertion_sort, bubble_sort]
    failed = 0
    for fn in funcs:
        print(f"--- {fn.__name__} ---")
        for nums in cases:
            original = list(nums)
            got = fn(nums)
            expect = sorted(nums)
            ok = got == expect and nums == original
            failed += 0 if ok else 1
            note = "" if nums == original else "  （原列表被改了）"
            print(f"{nums} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}{note}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
