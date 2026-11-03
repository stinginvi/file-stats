# 二叉树遍历练习（含 LC 94 中序遍历）。
# 测试已写好，你只需要完成 5 个函数。

from collections import deque


class TreeNode:
    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    """前序：根 → 左 → 右。"""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode | None) -> list[int]:
    """中序：左 → 根 → 右。"""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: TreeNode | None) -> list[int]:
    """后序：左 → 右 → 根。"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root: TreeNode | None) -> list[int]:
    """层序：一层一层从左到右。用队列，不用递归。"""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """中序遍历的迭代写法：用栈模拟递归。"""
    result = []
    stack = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result


def build_tree() -> TreeNode:
    """
           1
          / \
         2   3
        / \
       4   5
    """
    return TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))


if __name__ == "__main__":
    root = build_tree()
    cases = [
        ("preorder", preorder, [1, 2, 4, 5, 3]),
        ("inorder", inorder, [4, 2, 5, 1, 3]),
        ("postorder", postorder, [4, 5, 2, 3, 1]),
        ("level_order", level_order, [1, 2, 3, 4, 5]),
        ("inorder_iterative", inorder_iterative, [4, 2, 5, 1, 3]),
    ]
    failed = 0
    for name, fn, expect in cases:
        got = fn(root)
        ok = got == expect
        failed += 0 if ok else 1
        print(f"{name:18} 期望 {expect} 实际 {got} {'OK' if ok else 'FAIL'}")

    # 空树
    for name, fn, _ in cases:
        got = fn(None)
        ok = got == []
        failed += 0 if ok else 1
        print(f"{name:18} 空树 期望 [] 实际 {got} {'OK' if ok else 'FAIL'}")

    print(f"\n总计：{'全部通过' if failed == 0 else f'{failed} 项失败'}")
