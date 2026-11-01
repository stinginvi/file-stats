import argparse

from stats import FileStats
from utils import format_size


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="统计目录下的文件数量、大小和扩展名分布")
    parser.add_argument("--dir", default=".", help="要统计的目录（默认当前目录）")
    parser.add_argument("--top", type=int, default=5, help="显示最大的前 N 个文件（默认 5）")
    parser.add_argument("--output", default=None, help="把结果写成 JSON 报告")
    return parser


def print_report(stats: FileStats, top_n: int) -> None:
    r = stats.summary(top_n=top_n)
    print(f"文件数：{r['files']}")
    print(f"总大小：{format_size(r['total_size'])}")

    print("\n扩展名分布：")
    for ext, count in sorted(r["by_ext"].items(), key=lambda kv: kv[1], reverse=True):
        print(f"  {ext:<15} {count:>5}")

    print(f"\nTop {top_n} 大文件：")
    for name, size in r["top_files"]:
        print(f"  {name:<50} {format_size(size):>10}")
