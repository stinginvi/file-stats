class StatsError(Exception):
    """统计模块的自定义异常。"""
    pass


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为 0")
        # TODO: 打印提示，返回 None
        return None
    else:
        # TODO: 打印 "计算成功"，返回 result
        print("计算成功")
        return result
    finally:#先于 return 执行，但晚于 except 执行
        # TODO: 打印 "divide 结束"
        print("divide 结束")


def parse_int(text):
    # TODO: 用 try/except ValueError
    # 成功返回 int(text)
    # 失败打印 f"{text!r} 不是合法整数"，返回 None
    try:
        return int(text)
    except ValueError:
        print(f"{text!r} 不是合法整数")
        return None


def check_path(path):
    # TODO: path 是空字符串或 None 时，raise StatsError("路径不能为空")
    if path is None or path == "":
        raise StatsError("路径不能为空")


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))
    print(parse_int("42"))
    print(parse_int("abc"))

    try:
        check_path("")
    except StatsError as e:
        print("路径错误：", e)

# 预期输出（顺序不能错）
#
# 计算成功
# divide 结束
# 5.0
# 除数不能为 0
# divide 结束
# None
# 42
# 'abc' 不是合法整数
# None
# 路径错误： 路径不能为空