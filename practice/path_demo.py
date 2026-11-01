# 写一个脚本，把当前目录下所有文件的「相对路径 + 字节数」打印出来：

from pathlib import Path
root = Path(".")
for p in root.rglob("*"):
    if p.is_file():
        print(p.relative_to(root), p.stat().st_size)
        # TODO: 打印 p.relative_to(root) 和 p.stat().st_size
