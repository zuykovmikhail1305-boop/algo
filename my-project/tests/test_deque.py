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
    assert d.capacity == 1
    assert d[0] == 1


def test_pop_left():
    d = Deque_ended(5)
    d.add_left(1)
    d.add_left(2)
    d.pop_left()
    # слева лежала 2, её и сняли — осталась 1
    assert d.capacity == 1
    assert d[0] == 1


def test_getitem():
    d = Deque_ended(5)
    d.add_right(1)
    d.add_right(2)
    assert d[0] == 1
    assert d[1] == 2


def test_new_deque_is_empty():
    d = Deque_ended(5)
    assert d.is_empty()
    assert not d.is_full()


def test_mixed_left_and_right():
    d = Deque_ended(5)
    d.add_right(2)
    d.add_left(1)
    d.add_right(3)
    assert [d[i] for i in range(3)] == [1, 2, 3]


def test_negative_index():
    d = Deque_ended(5)
    for v in (1, 2, 3):
        d.add_right(v)
    assert d[-1] == 3
    assert d[-3] == 1


@pytest.mark.parametrize("key", [3, 10, -4])
def test_index_out_of_range(key):
    d = Deque_ended(5)
    for v in (1, 2, 3):
        d.add_right(v)
    with pytest.raises(IndexError):
        d[key]


def test_index_on_empty_deque():
    with pytest.raises(IndexError):
        Deque_ended(5)[0]


@pytest.mark.parametrize("key", ["0", 1.0, None, slice(0, 1)])
def test_index_must_be_int(key):
    d = Deque_ended(5)
    d.add_right(1)
    with pytest.raises(TypeError):
        d[key]


def test_fill_to_full_with_wraparound():
    # правый край упрётся в конец массива и перейдёт в начало
    d = Deque_ended(5)
    for v in (3, 4, 5):
        d.add_right(v)
    for v in (2, 1):
        d.add_left(v)
    assert d.is_full()
    assert [d[i] for i in range(5)] == [1, 2, 3, 4, 5]


def test_add_right_to_full_raises():
    d = Deque_ended(2)
    d.add_right(1)
    d.add_right(2)
    with pytest.raises(OverflowError):
        d.add_right(3)


def test_add_left_to_full_raises():
    d = Deque_ended(2)
    d.add_left(1)
    d.add_left(2)
    with pytest.raises(OverflowError):
        d.add_left(3)


@pytest.mark.parametrize("method", ["pop_left", "pop_right"])
def test_pop_from_empty_raises(method):
    d = Deque_ended(3)
    with pytest.raises(ValueError):
        getattr(d, method)()


def test_empty_after_popping_everything():
    d = Deque_ended(3)
    d.add_right(1)
    d.add_left(2)
    d.pop_right()
    d.pop_left()
    assert d.is_empty()


def test_reuse_after_pops():
    # после снятий освободившиеся ячейки должны снова быть доступны
    d = Deque_ended(3)
    for _ in range(10):
        d.add_right(1)
        d.add_right(2)
        d.add_left(0)
        assert d.is_full()
        assert [d[i] for i in range(3)] == [0, 1, 2]
        d.pop_left()
        d.pop_right()
        d.pop_right()
        assert d.is_empty()
