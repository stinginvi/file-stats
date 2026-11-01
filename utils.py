"""通用工具函数。"""


def format_size(num_bytes: int) -> str:
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
