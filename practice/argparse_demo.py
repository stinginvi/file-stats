import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="argparse 练习")
parser.add_argument("--dir",type=Path, default=".", help="要统计的目录")     # TODO 补 type/默认值
parser.add_argument("--top", type=int, default=5, help="前 N 个")
parser.add_argument("--output",type=Path, default=None, help="输出文件")

args = parser.parse_args()
print("dir =", args.dir)
print("top =", args.top)
print("output =", args.output)