import logging
from pathlib import Path

from cli import build_parser, print_report
from stats import FileStats, StatsError

logger = logging.getLogger(__name__)


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        filename="file-stats.log",
        encoding="utf-8",
    )

    parser = build_parser()
    args = parser.parse_args()

    if args.top <= 0:
        parser.error("--top 必须是正整数")

    root = Path(args.dir)
    if not root.is_dir():
        parser.error(f"目录不存在：{args.dir}")

    logger.info("开始统计目录：%s", root)

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
    # 把 main() 的返回值变成进程退出码：0 成功、1 失败，方便脚本调用
    raise SystemExit(main())
