# 骨架 + 测试：
# 给你一个整数数组 nums。如果任一值在数组中出现至少两次，返回 True；如果每个元素互不相同，返回 False。
def has_duplicate_set(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False



def has_duplicate_sort(nums):
    # TODO：注意 nums.sort() 会修改原列表
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]
    for nums, expected in cases:
        a = has_duplicate_set(nums.copy())
        b = has_duplicate_sort(nums.copy())
        print(f"集合={a}  排序={b}  期望={expected}")

# ▎ 为什么传 nums.copy()：sort() 会原地修改，测试用例要复用；set 解法本身不改原数组。