import pytest

from queue_with_stacks import Stack, Node, PseudoQueue

def test_create_node():
    one = Node(1)
    actual= one.value
    expected = 1
    assert actual == expected


def test_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    pseudo.enqueue(15)
    pseudo.enqueue(10)
    pseudo.enqueue(5)
    expected = 5
    actual = pseudo.inbox.peek()
    assert actual == expected









def test_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(20)
    pseudo.enqueue(15)
    pseudo.enqueue(10)
    pseudo.enqueue(5)
    expected = 5
    actual = pseudo.dequeue(5)
    assert actual == expected





# # Test 1
# def test_push_one():
#     stack = Stack()
#     stack.push(1)
#     expected = 1
#     actual = stack.peek()
#     assert actual == expected

# # Test 2
# def test_push_multiple():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     expected = 3
#     actual = stack.peek()
#     assert actual == expected

# # Test 3
# def test_pop_off():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.pop()
#     expected = 1
#     actual = stack.peek()
#     assert actual == expected

# # Test 4

# # Test 5
# def test_peek_next_item():
#     stack = Stack()
#     stack.push(1)
#     actual = stack.peek()
#     expected = 1
#     assert actual == expected

# # Test 6

# # Test 7
# def test_peek_empty_exception():
#     stack= Stack()
#     stack.push(1)
#     stack.pop()
#     actual = stack.peek()
#     expected = "empty stack"
#     assert actual == expected

# #### Queue Tests

# # Test 8
# def test_enqueue():
#     q = Queue()
#     q.enqueue("apple")
#     actual = q.peek()
#     expected = "apple"
#     assert actual == expected

# # Test 9
# def test_dequeue():
#     q = Queue()
#     q.enqueue("apple")
#     q.enqueue("banana")
#     actual = q.dequeue()
#     expected = "apple"
#     assert actual == expected

# #Test 11
# def test_peek():
#     q = Queue()
#     q.enqueue("apple")
#     q.enqueue("banana")
#     q.enqueue("cucumber")
#     actual = q.peek()
#     expected = "apple"
#     assert actual == expected

# # Test 12
# def test_exhausted():
#     q = Queue()
#     q.enqueue("apple")
#     q.enqueue("banana")
#     q.enqueue("cucumber")
#     q.dequeue()
#     q.dequeue()
#     q.dequeue()
#     actual = q.is_empty()
#     expected = True
#     assert actual == expected

# # Test 14
# def test_error_deque():
#     q = Queue()
#     q.enqueue("apple")
#     q.dequeue()
#     q.dequeue()
#     actual = q.peek()
#     expected = "empty queue"
#     assert actual == expected

