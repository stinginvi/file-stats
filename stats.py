# 先在 stats.py 顶部定义异常

import json                     # 文件顶部导入
from pathlib import Path

from utils import format_size     # 复用 Day 1 写的函数


class StatsError(Exception):
    """统计模块的自定义异常。"""


# FileStats 里用到的 FileNotFoundError、NotADirectoryError 是内置异常，语义清晰，保留；
# 只是「写报告失败」这种业务错误才包成 StatsError。


class FileStats:
    def __init__(self, path):
        self.root = Path(path)
        # 校验 self.root.exists() / is_dir()，抛对应异常
        if not self.root.exists():
            raise FileNotFoundError(f"{path!r} 不存在")
        if not self.root.is_dir():
            raise NotADirectoryError(f"{path!r} 不是目录")

    def _iter_files(self):
        """生成 root 下所有文件，跳过目录。"""
        for p in self.root.rglob("*"):
            if p.is_file():
                yield p  # 遍历文件，一边生成一边返回结果

    def summary(self) -> dict:
        # 遍历一次文件，stat 一次，同时收集计数/总大小/扩展名/排序数据
        pairs = []          # [(相对路径, 大小), ...]
        by_ext = {}
        for p in self._iter_files():
            try:
                size = p.stat().st_size
            except OSError:
                continue     # 没权限或断开的链接，跳过
            # by_ext 用 dict.get(key, 0) + 1 累积
            ext = p.suffix.lower() or "(无扩展名)"
            by_ext[ext] = by_ext.get(ext, 0) + 1
            pairs.append((str(p.relative_to(self.root)), size))

        count = len(pairs)
        total_size = sum(size for _, size in pairs)
        # 排序：pairs.sort(key=lambda x: x[1], reverse=True)，
        # lambda x: x[1] 就是"按每项的第 2 个元素（大小）排"
        pairs.sort(key=lambda x: x[1], reverse=True)
        # 取前 N：pairs[:5]，切片自动截断，不用判断长度
        top_files = pairs[:5]
        return {
            "files": count,
            "total_size": total_size,
            "by_ext": by_ext,
            "top_files": top_files,
        }

    def to_json(self, path) -> Path:
        """把统计结果写成 JSON 报告，返回写入的绝对路径。"""
        out = Path(path)
        data = self.summary()      # 先算再写，避免把正在创建的报告文件算进去
        try:
            # Path.open() 和内置 open() 用法一样，也支持 with
            with out.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            # 写报告失败属于业务错误，包成 StatsError
            # from e 保留原始异常链，以后排查能看到真正原因
            raise StatsError(f"写入报告失败：{e}") from e
        return out.resolve()


if __name__ == "__main__":
    # 测试代码
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

    # 写 JSON 报告
    out = s.to_json("report.json")
    print("报告已写入：", out)

    with open(out, encoding="utf-8") as f:
        back = json.load(f)
    print("读回的文件数：", back["files"])
    print("顶层键：", list(back.keys()))
    print("top_files 的类型：", type(back["top_files"][0]))

    # 场景 2：路径是文件，不是目录
    try:
        FileStats("stats.py")
    except NotADirectoryError as e:
        print("不是目录：", e)

    # 场景 3：输出路径的父目录不存在
    try:
        s.to_json("no_such_dir/report.json")
    except StatsError as e:
        print("写入失败：", e)

    # 场景 4：输出路径本身是个目录
    try:
        s.to_json(".")
    except StatsError as e:
        print("写入失败：", e)