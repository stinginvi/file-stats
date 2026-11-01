# file-stats

统计指定目录的文件数量、总大小、扩展名分布和最大的前 N 个文件，支持导出 JSON 报告。

## 功能

- 递归遍历目录，统计文件数与总大小
- 按扩展名统计分布（统一小写，无扩展名归为 `(无扩展名)`）
- 按大小降序输出 Top N 大文件
- 可选把结果写成 UTF-8 的 JSON 报告

## 环境要求

- Python 3.10 及以上
- 无第三方依赖，只用标准库

## 安装

```bash
git clone https://github.com/stinginvi/file-stats.git
cd file-stats

python -m venv .venv
source .venv/Scripts/activate     # Git Bash
# .venv\Scripts\activate          # CMD
# .venv\Scripts\Activate.ps1      # PowerShell

pip install -r requirements.txt
```

> 如果还没有 `requirements.txt`，当前版本没有第三方依赖，可以跳过安装步骤。

## 用法

```bash
# 统计当前目录，显示最大的 5 个文件
python main.py --dir . --top 5

# 统计并把结果写成 JSON 报告
python main.py --dir . --top 5 --output report.json

# 查看帮助
python main.py -h
```

### 参数

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `--dir` | 字符串 | `.` | 要统计的目录 |
| `--top` | 整数 | `5` | 终端显示最大的前 N 个文件，必须 > 0 |
| `--output` | 字符串 | `None` | 给定路径时导出 JSON 报告 |

## 示例输出

```text
文件数：84
总大小：75.8 KB

扩展名分布：
  (无扩展名)             49
  .sample            14
  .py                13
  .pyc                3
  .json               2
  .xml                2
  .iml                1

Top 3 大文件：
  __pycache__/stats.cpython-314.pyc                      6.2 KB
  .git/hooks/pre-rebase.sample                           4.8 KB
  .git/hooks/fsmonitor-watchman.sample                   4.5 KB
```

JSON 报告结构：

```json
{
  "files": 84,
  "total_size": 77642,
  "by_ext": {
    ".py": 13,
    ".json": 2
  },
  "top_files": [
    ["__pycache__/stats.cpython-314.pyc", 6342],
    [".git/hooks/pre-rebase.sample", 4895]
  ]
}
```

> JSON 没有元组类型，所以 `top_files` 里的元组读回来会变成列表。

## 项目结构

```text
file-stats/
├── main.py          # 命令行入口：解析参数、打印报表
├── stats.py         # FileStats：统计逻辑与 JSON 导出
├── utils.py         # 通用工具：format_size
├── practice/        # 学习过程中的练习代码
├── .gitignore
└── README.md
```

## 退出码

| 退出码 | 含义 |
|---|---|
| `0` | 成功 |
| `1` | 运行时错误（如写入报告失败） |
| `2` | 参数错误（目录不存在、`--top` 非法） |

## 已知限制

- 当前会统计 `.git/`、`__pycache__/`、`.venv/` 等目录，尚未提供排除参数
- 如果目标目录里已经存在上一次生成的 `report.json`，它会被算进统计结果
- 中文扩展名分类 `(无扩展名)` 在终端里占两个字符宽，与其他行不完全对齐

## 测试

暂无自动化测试，计划在后续版本加入 pytest 用例。
