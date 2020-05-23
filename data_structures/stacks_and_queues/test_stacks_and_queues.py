import pytest

from stacks_and_queues import Queue, Stack


def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_peek_when_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()


def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_push_one_item():
    fruits = Stack()
    fruits.push('apple')
    expected = 'apple'
    actual = fruits.peek()
    assert actual == expected

def test_pop_items():
    dishes = Stack()
    dishes.push('yellow dish')
    dishes.push('mom dish')
    dishes.push('cat dish')
    expected = 'mom dish'
    dishes.pop()
    actual = dishes.pop()
    assert actual == expected

def test_is_empty():
    paranths = Stack()
    paranths.push('(')
    paranths.push(')')
    paranths.pop()
    paranths.pop()
    actual = paranths.is_empty()
    expected = True
    assert actual == expected
