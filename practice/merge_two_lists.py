# 题目：合并两个升序链表（LC 21），返回合并后的升序链表。
# 要求：复用原节点，不新建值节点。时间 O(m+n)，空间 O(1)。
# 测试已写好，你只需要完成 merge_two_lists 函数。

from linked_list import LinkedList, Node


def merge_two_lists(list1: Node | None, list2: Node | None) -> Node | None:
    """合并两个有序链表。dummy 是哨兵节点，tail 是拼接用的尾巴。"""
    dummy = Node(0)
    tail = dummy
    # TODO 1: 两个链表都不空时，比较当前节点的值，把小的挂到 tail 后面
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    # TODO 2: 谁还剩下，就把剩下的一整串接上去
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    # TODO 3: 返回真正的头（不是 dummy）
    return dummy.next


def make_list(nums: list[int]) -> Node | None:
    ll = LinkedList()
    for x in nums:
        ll.append(x)
    return ll.head


def read_list(head: Node | None) -> list[int]:
    ll = LinkedList()
    ll.head = head
    return ll.to_list()


if __name__ == "__main__":
    cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [1, 2, 3], [1, 2, 3, 5]),
    ]
    failed = 0
    for a, b, expect in cases:
        got = read_list(merge_two_lists(make_list(a), make_list(b)))
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{a} + {b} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
