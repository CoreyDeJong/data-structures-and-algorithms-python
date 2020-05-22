import pytest
from challenges.ll_merge.__pycache__.ll_merge import LinkedList, Node


### ll Merge #####

def test_linked_list_str(list1_odd, list2_odd):
    ll = LinkedList()
    ll.mergeLists(list1_odd)
    ll.mergeLists(list2_odd)
    # assert str(ll) == "{ bananas } -> { apples } -> NULL"






# ## linkedlist insert
# def test_insert_empty():
#     ll = LinkedList()
#     ll.insert("apples")
#     assert ll.head.value == "apples"

# ## linkedlist
# def test_insert_full():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     assert ll.head.value == "bananas"
#     assert ll.head.next.value == "apples"


# #### Append #######

# def test_append_1():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     ll.append("pineapple")
#     assert str(ll) == "{ bananas } -> { apples } -> { pineapple } -> NULL"


# #### Insert Before #######

# def test_insert_1():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     ll.insertBefore("pineapple")
#     assert str(ll) == "{ pineapple } -> { bananas } -> { apples } -> NULL"

# #### Insert After #######

# def test_insert_1():
#     ll = LinkedList()
#     ll.insert("a")
#     ll.insert("b")
#     ll.insertAfter("b", "c")
#     assert str(ll) == "{ b } -> { c } -> { a } -> NULL"


@pytest.fixture()
def list1_odd():
    ll = LinkedList()
    ll.insert("1")
    ll.insert("3")
    ll.insert("2")

@pytest.fixture()
def list1_even():
    ll = LinkedList()
    ll.insert("1")
    ll.insert("3")


@pytest.fixture
def list2_odd():
    ll = LinkedList()
    ll.insert("5")
    ll.insert("9")
    ll.insert("4")
    return ll

@pytest.fixture
def list2_even():
    ll = LinkedList()
    ll.insert("5")
    ll.insert("9")
    return ll