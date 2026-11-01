def remove_duplicates(nums):
    if not nums:
        return 0              # 空数组返回零

    k = 1                   # 已经保留了第一个

    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:   # 跟已保留的最后一个比
            nums[k] = nums[i]    # 新元素写到上一个新位置后面
            k += 1

    return k


def check(nums):
    k = remove_duplicates(nums)
    print(f"k={k}, 前 k 个={nums[:k]}")

if __name__ == "__main__":
    check([1, 1, 2])                                  # 期望 k=2, [1, 2]
    check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])             # 期望 k=5, [0, 1, 2, 3, 4]
    check([])                                         # 期望 k=0
    check([1])                                        # 期望 k=1
