
from pathlib import Path


class FileStats:
    def __init__(self, path):
        self.root = Path(path)
        # TODO: 校验 self.root.exists() / is_dir()，抛对应异常
        if not self.root.exists():
            raise FileNotFoundError(f"{path!r} 不存在")
        if not self.root.is_dir():
            raise NotADirectoryError(f"{path!r} 不是目录")

    def _iter_files(self):
        """生成 root 下所有文件，跳过目录。"""
        for p in self.root.rglob("*"):
            if p.is_file():
                yield p

    def summary(self) -> dict:
        # 遍历一次文件，stat 一次，同时收集计数/总大小/扩展名/排序数据
        pairs = []          # [(相对路径, 大小), ...]
        by_ext = {}
        for p in self._iter_files():
            try:
                size = p.stat().st_size
            except OSError:
                continue     # 没权限或断开的链接，跳过
            ext = p.suffix.lower() or "(无扩展名)"
            by_ext[ext] = by_ext.get(ext, 0) + 1
            pairs.append((str(p.relative_to(self.root)), size))

        count = len(pairs)
        total_size = sum(size for _, size in pairs)
        pairs.sort(key=lambda x: x[1], reverse=True)
        top_files = pairs[:5]
        return {
            "files": count,
            "total_size": total_size,
            "by_ext": by_ext,
            "top_files": top_files,
        }

# 几个提示：
# - by_ext 用 dict.get(key, 0) + 1 累积
# - 排序：pairs.sort(key=lambda x: x[1], reverse=True)，lambda x: x[1] 就是"按每项的第 2 个元素（大小）排"
# - f.stat().st_size 可能抛 PermissionError，用 try/except OSError 包住，continue
# - 取前 N：pairs[:5]，切片自动截断，不用判断长度
#
# 测试代码（照抄）

from basics import format_size     # 复用 Day 1 写的函数

if __name__ == "__main__":
    s = FileStats(".")
    r = s.summary()

    print("文件数：", r["files"])
    print("总大小：", format_size(r["total_size"]))
    print("扩展名分布：", r["by_ext"])
    print("Top 5：")
    for name, size in r["top_files"]:
        print(f"  {name}  {format_size(size)}")

    # 错误场景
    try:
        FileStats("no_such_dir")
    except FileNotFoundError as e:
        print("目录不存在：", e)