from dataclasses import dataclass


# ---------- __init__ 示例 ----------
class Dog:
    def __init__(self, name, age):
        self.name = name            # 实例属性
        self.age = age


d1 = Dog("Buddy", 3)
print(d1.name)                      # Buddy


# ---------- 类属性陷阱 ----------
class Team:
    members = []                    # ⚠️ 类属性：所有实例共享同一个列表

    def __init__(self, name):
        self.name = name


t1 = Team("Alpha")
print(t1.name)
t2 = Team("Beta")
t1.members.append("Alice")
print(t2.members)                   # ['Alice']，t2 被污染了


# ---------- 继承 ----------
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name)      # 关键：先让父类初始化
        self.indoor = indoor


c = Cat("Kitty", True)
print(c.name, c.indoor)             # Kitty True


# ---------- dataclass ----------
@dataclass
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)
print(p)                            # Point(x=1.0, y=2.0)


# ---------- 练习：银行账户 ----------
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount

    def __str__(self) -> str:
        return f"{self.owner} 的余额：{self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, rate: float = 0.03):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self) -> None:
        self.balance += self.balance * self.rate


if __name__ == "__main__":
    acc = BankAccount("张三", 100)
    acc.deposit(50)
    print(acc)                          # 张三 的余额：150.00

    acc.withdraw(30)
    print(acc.balance)                  # 120（传入的是整数，所以结果是整数）

    try:
        acc.withdraw(9999)
    except ValueError as e:
        print("取款失败：", e)          # 取款失败： 余额不足

    try:
        acc.deposit(-10)
    except ValueError as e:
        print("存款失败：", e)          # 存款失败： 存款金额必须大于 0

    s = SavingsAccount("李四", 1000, 0.05)
    s.add_interest()
    print(s)                            # 李四 的余额：1050.00
