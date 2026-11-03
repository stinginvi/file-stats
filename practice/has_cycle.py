# 题目：判断链表是否有环（LC 141）。
# 要求：时间 O(n)，空间 O(1)（不要用 set 记录走过的节点）。
# 测试已写好，你只需要完成 has_cycle 函数。

from linked_list import Node


def has_cycle(head: Node | None) -> bool:
    """快慢指针：慢的走 1 步，快的走 2 步，有环必相遇。"""
    slow = head
    fast = head
    # TODO: 循环条件怎么写，才能保证 fast.next.next 不越界？
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def make_cycle(nums: list[int], pos: int) -> Node | None:
    """建链表，并让最后一个节点指回下标为 pos 的节点（pos=-1 表示无环）。"""
    if not nums:
        return None
    nodes = [Node(nums[0])]
    for x in nums[1:]:
        nodes.append(Node(x))
        nodes[-2].next = nodes[-1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2, 3], -1, False),
        ([], -1, False),
    ]
    failed = 0
    for nums, pos, expect in cases:
        got = has_cycle(make_cycle(nums, pos))
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{nums} 环在 {pos} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
