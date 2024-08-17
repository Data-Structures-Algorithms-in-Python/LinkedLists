from behave import *

from src.linked_lists.main import LinkedList, Node

use_step_matcher("re")


@given("an empty linked list")
def step_given_any_empty_linked_list(context):
    """
    :type context: behave.runner.Context
    """
    context.empty_linked_list = LinkedList(None)


@when("add a new node with 5")
def step_when_add_new_node(context):
    """
    :type context: behave.runner.Context
    """
    context.new_node = Node(5)
    context.empty_linked_list.head = context.new_node
    context.empty_linked_list.tail = context.new_node
    context.empty_linked_list.length = 1


@then("new_node should be added to empty linked list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.empty_linked_list.head.value == 5
    assert context.empty_linked_list.tail.value == 5
    assert context.empty_linked_list.length == 1


@given("a linked list with nodes")
def step_given_non_empty_linked_list(context):
    """
    :type context: behave.runner.Context
    """
    context.linked_list = LinkedList(None)
    context.linked_list.append_node(2)


@when("append a new node")
def step_when_append_new_node(context):
    """
    :type context: behave.runner.Context
    """
    context.linked_list.append_node(12)


@then("new_node should be appended to non-empty linked list")
def step_then_new_node_appended_in_linked_list(context):
    """
    :type context: behave.runner.Context
    """
    assert context.linked_list.head.value == 2
    assert context.linked_list.tail.value == 12
    assert context.linked_list.length == 2
    assert context.linked_list.print_linked_list() == ["2", "12"]
