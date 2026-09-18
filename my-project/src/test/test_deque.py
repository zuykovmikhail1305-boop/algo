import pytest
from my_project.data.deque import Deque_ended


def test_add_right():
    d = Deque_ended(5)
    d.add_right(1)
    d.add_right(2)
    assert d[0] == 1
    assert d[1] == 2


def test_add_left():
    d = Deque_ended(5)
    d.add_left(1)
    d.add_left(2)
    assert d[0] == 2
    assert d[1] == 1


def test_pop_right():
    d = Deque_ended(5)
    d.add_right(1)
    d.add_right(2)
    d.pop_right()
    assert d[0] == 1


def test_pop_left():
    d = Deque_ended(5)
    d.add_left(1)
    d.add_left(2)
    d.pop_left()
    assert d[0] == 2



def test_getitem():
    d = Deque_ended(5)
    d.add_right(1)
    d.add_right(2)
    assert d[0] == 1
    assert d[1] == 2
