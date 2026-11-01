import argparse
from pathlib import Path

from stats import FileStats, StatsError
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

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.top <= 0:
        parser.error("--top 必须是正整数")

    root = Path(args.dir)
    if not root.is_dir():
        parser.error(f"目录不存在：{args.dir}")

    try:
        stats = FileStats(root)
        print_report(stats, args.top)
        if args.output:
            out = stats.to_json(args.output, top_n=args.top)
            print(f"\n报告已写入：{out}")
    except StatsError as e:
        print(f"错误：{e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# raise SystemExit(main()) 的作用：把 main() 的返回值变成进程退出码，0 成功、1 失败，方便脚本调用。