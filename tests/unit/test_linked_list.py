from src.linked_lists.main import LinkedList


def test_create_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_create_linked_list_with_one_node():
    linked_list = LinkedList(4)
    assert linked_list.head.value == 4
    assert linked_list.tail.value == 4
    assert linked_list.length == 4


def test_create_linked_list_with_multiple_nodes():
    linked_list = LinkedList(4)
    linked_list.append_node(5)
    linked_list.append_node(6)
    assert linked_list.head.value == 4
    assert linked_list.tail.value == 6
    assert linked_list.length == 3
    assert linked_list.print_linked_list() == ["4", "5", "6"]
