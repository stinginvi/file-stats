# 题目：反转一个单链表（LC 206）。
# 要求：原地反转，不新建节点。时间 O(n)，空间 O(1)。
# 测试已写好，你只需要完成 reverse_list 函数。

from linked_list import LinkedList, Node


def reverse_list(head: Node | None) -> Node | None:
    """反转链表，返回新的头节点。"""
    prev = None
    cur = head
    while cur is not None:
        # TODO 1: 先保存 cur.next（思考题 2 的答案就是这一步的理由）
        next_node = cur.next
        # TODO 2: 让当前节点掉头，指向 prev
        cur.next = prev
        # TODO 3: prev 和 cur 各往前走一格
        prev = cur
        cur = next_node
    return prev


def make_list(nums: list[int]) -> Node | None:
    ll = LinkedList()
    for x in nums:
        ll.append(x)
    return ll.head


def read_list(head: Node | None) -> list[int]:
    ll = LinkedList()
    ll.head = head
    return ll.to_list()


def reverse_list_recursive(head: Node | None) -> Node | None:
    """递归版：先让后面的全部反转好，再处理自己。时间 O(n)，空间 O(n)（调用栈）。"""
    # ① 终止条件：空链表，或只剩一个节点（它已经是反转好的头）
    if head is None or head.next is None:
        return head
    # ② 信任子问题：head.next 开头的部分反转好了，new_head 是新头
    new_head = reverse_list_recursive(head.next)
    # ③ 本层做什么：让「下一个节点」指回自己，再切断自己的 next
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    funcs = [reverse_list, reverse_list_recursive]
    failed = 0
    for fn in funcs:
        print(f"--- {fn.__name__} ---")
        for nums, expect in cases:
            got = read_list(fn(make_list(nums)))
            ok = got == expect
            failed += 0 if ok else 1
            print(f"{nums} 反转 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
