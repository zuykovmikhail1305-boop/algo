import random

import pytest
from my_project.data.AVL import AVL

#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 7   9
# при такой вставке повороты не нужны — дерево сразу сбалансировано
VALUES = [5, 3, 8, 1, 4, 7, 9]


def build(values):
    t = AVL()
    for v in values:
        t.insert(v)
    return t


@pytest.fixture
def tree():
    return build(VALUES)


def height(node):
    # высота листа 0, пустого поддерева -1 — так же, как считается depht
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def assert_valid(t, balanced=True):
    # порядок дерева поиска и правильные .root;
    # balanced=True — ещё depht каждого узла и разница высот детей не больше 1
    def walk(node, parent, low, high):
        if node is None:
            return
        assert node.root is parent, f"у узла {node.value} неверный .root"
        assert (low is None or node.value > low) and (high is None or node.value < high), (
            f"узел {node.value} нарушает порядок дерева"
        )
        if balanced:
            assert node.depht == height(node), f"у узла {node.value} неверный depht"
            diff = height(node.left) - height(node.right)
            assert abs(diff) <= 1, f"узел {node.value} разбалансирован: {diff}"
        walk(node.left, node, low, node.value)
        walk(node.right, node, node.value, high)

    walk(t.head, None, None, None)


# ---------- пустое дерево и одна вставка ----------


def test_empty_tree():
    t = AVL()
    assert t.head is None
    assert not t.search(1)


@pytest.mark.parametrize("method", ["inorder", "preroder", "postorder", "level_order"])
def test_traversals_of_empty_tree(method):
    assert getattr(AVL(), method)() == []


def test_insert_first_value_becomes_head():
    t = build([10])
    assert t.head.value == 10
    assert t.head.root is None
    assert t.head.depht == 0


# ---------- вставка без поворотов ----------


@pytest.mark.parametrize("values", [[5, 3], [5, 8]])
def test_insert_two_values(values):
    t = build(values)
    assert t.head.value == 5
    assert t.head.depht == 1
    assert t.inorder() == sorted(values)
    assert_valid(t)


def test_insert_three_balanced():
    t = build([2, 1, 3])
    assert t.level_order() == [2, 1, 3]
    assert t.head.depht == 1
    assert_valid(t)


def test_insert_links_children(tree):
    assert tree.head.left.value == 3
    assert tree.head.right.value == 8
    assert tree.head.left.left.value == 1
    assert tree.head.right.right.value == 9


def test_depht_without_rotations(tree):
    assert tree.head.depht == 2
    assert tree.head.left.depht == 1
    assert tree.head.right.depht == 1
    assert tree.head.left.left.depht == 0
    assert tree.head.right.right.depht == 0


def test_tree_is_valid_after_insert(tree):
    assert_valid(tree)


def test_duplicate_is_ignored(tree):
    tree.insert(4)
    assert tree.inorder() == sorted(VALUES)
    assert_valid(tree)


# ---------- малые повороты ----------


def test_right_heavy_root_is_rotated():
    # 1           2
    #  \         / \
    #   2   →   1   3
    #    \
    #     3
    t = build([1, 2, 3])
    assert t.head.value == 2
    assert t.level_order() == [2, 1, 3]
    assert_valid(t)


def test_left_heavy_root_is_rotated():
    #     3       2
    #    /       / \
    #   2   →   1   3
    #  /
    # 1
    t = build([3, 2, 1])
    assert t.head.value == 2
    assert t.level_order() == [2, 1, 3]
    assert_valid(t)


def test_right_heavy_subtree_is_rotated():
    #   5               5
    #  / \             / \
    # 3   8      →    3   9
    #      \             / \
    #       9           8   10
    #        \
    #         10
    t = build([5, 3, 8, 9, 10])
    assert t.level_order() == [5, 3, 9, 8, 10]
    assert_valid(t)


def test_left_heavy_subtree_is_rotated():
    #       5           5
    #      / \         / \
    #     3   8  →    2   8
    #    /           / \
    #   2           1   3
    #  /
    # 1
    t = build([5, 3, 8, 2, 1])
    assert t.level_order() == [5, 2, 8, 1, 3]
    assert_valid(t)


def test_rotation_moves_middle_subtree_left():
    #   2                  4
    #  / \               /   \
    # 1   4      →      2     5
    #    / \           / \     \
    #   3   5         1   3     6
    #        \
    #         6
    # поддерево 3 переезжает от 4 к 2
    t = build([2, 1, 4, 3, 5, 6])
    assert t.head.value == 4
    assert t.level_order() == [4, 2, 5, 1, 3, 6]
    assert_valid(t)


def test_rotation_moves_middle_subtree_right():
    #       5              3
    #      / \           /   \
    #     3   6    →    2     5
    #    / \           /     / \
    #   2   4         1     4   6
    #  /
    # 1
    # поддерево 4 переезжает от 3 к 5
    t = build([5, 6, 3, 4, 2, 1])
    assert t.head.value == 3
    assert t.level_order() == [3, 2, 5, 1, 4, 6]
    assert_valid(t)


@pytest.mark.parametrize("n", [3, 7, 15, 100])
def test_ascending_inserts_stay_balanced(n):
    # вставка по возрастанию требует только левых малых поворотов
    t = build(range(1, n + 1))
    assert t.inorder() == list(range(1, n + 1))
    assert_valid(t)


@pytest.mark.parametrize("n", [3, 7, 15, 100])
def test_descending_inserts_stay_balanced(n):
    # вставка по убыванию требует только правых малых поворотов
    t = build(range(n, 0, -1))
    assert t.inorder() == list(range(1, n + 1))
    assert_valid(t)


def test_ascending_inserts_shape():
    t = build(range(1, 8))
    assert t.level_order() == [4, 2, 6, 1, 3, 5, 7]
    assert t.head.depht == 2


# ---------- обходы ----------


def test_inorder_is_sorted(tree):
    assert tree.inorder() == sorted(VALUES)


def test_preorder(tree):
    assert tree.preroder() == [5, 3, 1, 4, 8, 7, 9]


def test_postorder(tree):
    assert tree.postorder() == [1, 4, 3, 7, 9, 8, 5]


def test_level_order(tree):
    assert tree.level_order() == [5, 3, 8, 1, 4, 7, 9]


# ---------- поиск ----------


@pytest.mark.parametrize("value", VALUES)
def test_search_existing(tree, value):
    node = tree.search(value)
    assert node
    assert node.value == value


@pytest.mark.parametrize("value", [0, 2, 6, 10])
def test_search_missing(tree, value):
    assert not tree.search(value)


def test_search_after_rotations():
    t = build(range(1, 16))
    for v in range(1, 16):
        assert t.search(v).value == v
    assert not t.search(0)
    assert not t.search(16)


# ---------- удаление (без перебалансировки) ----------


def test_delete_leaf(tree):
    tree.delete(1)
    assert tree.inorder() == [3, 4, 5, 7, 8, 9]
    assert not tree.search(1)
    assert_valid(tree, balanced=False)


def test_delete_node_with_one_child(tree):
    tree.delete(1)
    tree.delete(3)
    assert tree.inorder() == [4, 5, 7, 8, 9]
    assert tree.head.left.value == 4
    assert_valid(tree, balanced=False)


def test_delete_node_with_two_children(tree):
    tree.delete(8)
    assert tree.inorder() == [1, 3, 4, 5, 7, 9]
    assert_valid(tree, balanced=False)


def test_delete_root(tree):
    tree.delete(5)
    assert tree.inorder() == [1, 3, 4, 7, 8, 9]
    assert tree.head.value == 7
    assert_valid(tree, balanced=False)


def test_delete_missing_value_changes_nothing(tree):
    tree.delete(42)
    assert tree.inorder() == sorted(VALUES)
    assert_valid(tree)


def test_delete_from_empty_tree():
    t = AVL()
    t.delete(1)
    assert t.head is None


def test_delete_only_node():
    t = build([1])
    t.delete(1)
    assert t.head is None


def test_delete_everything(tree):
    for v in [1, 9, 3, 7, 5, 4, 8]:
        tree.delete(v)
        assert_valid(tree, balanced=False)
    assert tree.head is None


def test_delete_after_rotations():
    t = build(range(1, 16))
    for v in [8, 1, 15, 4, 12]:
        t.delete(v)
        assert_valid(t, balanced=False)
    assert t.inorder() == [2, 3, 5, 6, 7, 9, 10, 11, 13, 14]


def test_random_inserts_and_deletes_keep_order():
    # здесь проверяется только порядок дерева и .root, а не баланс:
    # случайная вставка требует и больших поворотов
    rng = random.Random(7)
    for _ in range(100):
        values = rng.sample(range(100), rng.randint(1, 30))
        t = build(values)
        assert t.inorder() == sorted(values), values
        assert_valid(t, balanced=False)
        alive = set(values)
        for v in rng.sample(values, len(values)):
            t.delete(v)
            alive.discard(v)
            assert t.inorder() == sorted(alive), (values, v)
            assert_valid(t, balanced=False)
        assert t.head is None
