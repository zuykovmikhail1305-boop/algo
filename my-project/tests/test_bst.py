import pytest
from my_project.data.BST import BST

#         5
#       /   \
#      3     8
#     / \   / \
#    1   4 7   9
VALUES = [5, 3, 8, 1, 4, 7, 9]


@pytest.fixture
def tree():
    t = BST()
    for v in VALUES:
        t.insert(v)
    return t


def test_empty_tree():
    t = BST()
    assert t.head is None
    assert t.inorder() == []


def test_insert_first_value_becomes_head():
    t = BST()
    t.insert(10)
    assert t.head.value == 10


def test_insert_links_children(tree):
    assert tree.head.left.value == 3
    assert tree.head.right.value == 8
    assert tree.head.left.left.value == 1
    assert tree.head.right.right.value == 9


def test_inorder_is_sorted(tree):
    assert tree.inorder() == sorted(VALUES)


def test_preorder(tree):
    assert tree.preroder() == [5, 3, 1, 4, 8, 7, 9]


def test_postorder(tree):
    assert tree.postorder() == [1, 4, 3, 7, 9, 8, 5]


def test_level_order(tree):
    assert tree.level_order() == [5, 3, 8, 1, 4, 7, 9]


def test_duplicate_is_ignored(tree):
    tree.insert(4)
    assert tree.inorder() == sorted(VALUES)


@pytest.mark.parametrize("value", VALUES)
def test_search_existing(tree, value):
    node = tree.search(value)
    assert node
    assert node.value == value


@pytest.mark.parametrize("value", [0, 2, 6, 10])
def test_search_missing(tree, value):
    assert not tree.search(value)


def test_search_in_empty_tree():
    assert not BST().search(1)


def test_delete_leaf(tree):
    tree.delete(1)
    assert tree.inorder() == [3, 4, 5, 7, 8, 9]
    assert not tree.search(1)


def test_delete_node_with_one_child(tree):
    tree.delete(1)
    tree.delete(3)  # теперь у 3 остался только правый ребёнок 4
    assert tree.inorder() == [4, 5, 7, 8, 9]
    assert tree.head.left.value == 4


def test_delete_node_with_two_children(tree):
    tree.delete(8)
    assert tree.inorder() == [1, 3, 4, 5, 7, 9]


def test_delete_root(tree):
    tree.delete(5)
    assert tree.inorder() == [1, 3, 4, 7, 8, 9]
    assert tree.head.value not in (5, None)


def test_delete_everything(tree):
    for v in VALUES:
        tree.delete(v)
    assert tree.inorder() == []


def assert_valid(t):
    # каждый узел лежит в своих границах, а .root указывает на настоящего родителя
    def walk(node, parent, low, high):
        if node is None:
            return
        assert node.root is parent, f"у узла {node.value} неверный .root"
        assert (low is None or node.value > low) and (high is None or node.value < high), (
            f"узел {node.value} нарушает порядок дерева"
        )
        walk(node.left, node, low, node.value)
        walk(node.right, node, node.value, high)

    walk(t.head, None, None, None)


def build(values):
    t = BST()
    for v in values:
        t.insert(v)
    return t


def test_tree_is_valid_after_insert(tree):
    assert_valid(tree)


@pytest.mark.parametrize("method", ["inorder", "preroder", "postorder", "level_order"])
def test_traversals_of_empty_tree(method):
    assert getattr(BST(), method)() == []


def test_level_order_single_node():
    assert build([1]).level_order() == [1]


def test_level_order_unbalanced():
    #   4
    #  / \
    # 2   6
    #      \
    #       7
    #        \
    #         8
    assert build([4, 2, 6, 7, 8]).level_order() == [4, 2, 6, 7, 8]


def test_delete_missing_value_changes_nothing(tree):
    tree.delete(42)
    assert tree.inorder() == sorted(VALUES)
    assert_valid(tree)


def test_delete_from_empty_tree():
    t = BST()
    t.delete(1)
    assert t.head is None


def test_delete_only_node():
    t = build([1])
    t.delete(1)
    assert t.head is None
    assert t.inorder() == []


def test_delete_root_with_only_right_child():
    t = build([1, 2, 3])
    t.delete(1)
    assert t.head.value == 2
    assert t.inorder() == [2, 3]
    assert_valid(t)


def test_delete_root_with_only_left_child():
    t = build([3, 2, 1])
    t.delete(3)
    assert t.head.value == 2
    assert t.inorder() == [1, 2]
    assert_valid(t)


def test_delete_right_leaf_when_parent_has_no_left():
    t = build([1, 2])
    t.delete(2)
    assert t.inorder() == [1]
    assert t.head.right is None


def test_delete_left_leaf_when_parent_has_no_right():
    t = build([2, 1])
    t.delete(1)
    assert t.inorder() == [2]
    assert t.head.left is None


def test_delete_node_with_only_left_child(tree):
    tree.delete(9)
    tree.delete(8)  # у 8 остался только левый ребёнок 7
    assert tree.inorder() == [1, 3, 4, 5, 7]
    assert tree.head.right.value == 7
    assert_valid(tree)


def test_delete_successor_with_right_child():
    #     5
    #    / \
    #   2   8
    #      / \
    #     6   9
    #      \
    #       7
    t = build([5, 2, 8, 6, 9, 7])
    t.delete(5)  # на место 5 встаёт 6, а его ребёнок 7 — на место 6
    assert t.head.value == 6
    assert t.inorder() == [2, 6, 7, 8, 9]
    assert_valid(t)


def test_parent_links_after_deletes(tree):
    tree.delete(3)
    tree.delete(8)
    assert_valid(tree)
    tree.delete(4)
    tree.delete(9)
    assert_valid(tree)
    assert tree.inorder() == [1, 5, 7]


def test_deleted_value_is_not_found(tree):
    tree.delete(8)
    assert not tree.search(8)
    for v in [1, 3, 4, 5, 7, 9]:
        assert tree.search(v).value == v


def test_insert_after_delete(tree):
    tree.delete(8)
    tree.insert(8)
    tree.insert(6)
    assert tree.inorder() == [1, 3, 4, 5, 6, 7, 8, 9]
    assert_valid(tree)


def test_delete_everything_in_other_order(tree):
    for v in [1, 9, 3, 7, 5, 4, 8]:
        tree.delete(v)
        assert_valid(tree)
    assert tree.head is None


def test_random_inserts_and_deletes():
    import random

    rng = random.Random(7)
    for _ in range(100):
        values = rng.sample(range(100), rng.randint(1, 30))
        t = build(values)
        alive = set(values)
        for v in rng.sample(values, len(values)):
            t.delete(v)
            alive.discard(v)
            assert t.inorder() == sorted(alive), (values, v)
            assert_valid(t)
        assert t.head is None
