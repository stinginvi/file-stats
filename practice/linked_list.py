# 单链表练习：节点 + 基本操作。
# 测试已写好，你只需要完成 LinkedList 的 4 个方法。


class Node:
    def __init__(self, val: int, next: "Node | None" = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, val: int) -> None:
        """尾插：把 val 加到链表末尾。"""
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def prepend(self, val: int) -> None:
        """头插：把 val 加到链表开头。"""
        self.head = Node(val, self.head)

    def delete(self, val: int) -> bool:
        """删除第一个值为 val 的节点。删掉了返回 True，没找到返回 False。"""
        if self.head is None:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        prev, cur = self.head, self.head.next
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def to_list(self) -> list[int]:
        """转成 Python 列表，方便比较。"""
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for x in [1, 2, 3]:
        ll.append(x)
    print("append    ", ll.to_list(), "期望 [1, 2, 3]")

    ll.prepend(0)
    print("prepend   ", ll.to_list(), "期望 [0, 1, 2, 3]")

    ok = ll.delete(2)
    print("delete 2  ", ok, ll.to_list(), "期望 True [0, 1, 3]")

    ok = ll.delete(0)  # 删头节点
    print("delete 0  ", ok, ll.to_list(), "期望 True [1, 3]")

    ok = ll.delete(99)  # 不存在
    print("delete 99 ", ok, ll.to_list(), "期望 False [1, 3]")

    empty = LinkedList()
    print("empty     ", empty.to_list(), "期望 []")
