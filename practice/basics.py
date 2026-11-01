def average(nums):
    """返回平均值；空列表返回 None。"""
    if not nums:
        return None
    return sum(nums) / len(nums)


def filter_even(nums):
    """返回偶数组成的新列表，不修改原列表。"""
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result


def format_size(num_bytes):
    """把字节数格式化为 B / KB / MB / GB / TB。"""
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    index = 0

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    if index == 0:
        return f"{int(size)} B"
    return f"{size:.1f} {units[index]}"


if __name__ == "__main__":
    print(average([1, 2, 3]))          # 2.0
    print(average([]))                 # None
    print(filter_even([1, 2, 3, 4]))   # [2, 4]
    print(format_size(0))              # 0 B
    print(format_size(512))            # 512 B
    print(format_size(1536))           # 1.5 KB
    print(format_size(5 * 1024**3))    # 5.0 GB
