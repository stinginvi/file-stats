# 给你两个非递减整数数组 nums1 和 nums2，以及两个整数 m、n，分别表示 nums1 和 nums2 中的有效元素个数。
# nums1 的总长度是 m + n，其中前 m 个是有效数据，后 n 个是占位的 0。
# 要求把 nums2 合并进 nums1，使 nums1 成为有序数组。不要返回新数组，直接在 nums1 上改。
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1          # nums1 有效部分的末尾
    j = n - 1          # nums2 的末尾
    k = m + n - 1      # nums1 的最后一个空位

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # nums2 还有剩，直接搬过去
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

def check(nums1, m, nums2, n, expected):
    merge(nums1, m, nums2, n)
    ok = "✅" if nums1 == expected else "❌"
    print(f"{ok} 结果={nums1}  期望={expected}")


if __name__ == "__main__":
    check([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    check([1], 1, [], 0, [1])
    check([0], 0, [1], 1, [1])
    check([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])