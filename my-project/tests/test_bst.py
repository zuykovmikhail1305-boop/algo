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
