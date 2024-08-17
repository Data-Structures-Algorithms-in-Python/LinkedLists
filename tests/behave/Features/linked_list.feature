# Created by Sunil Sharma at 8/17/24
Feature: Different operations on a linked list

  Scenario: Add a new node to an empty linked list
    Given an empty linked list
    When add a new node with 5
    Then new_node should be added to empty linked list

    Scenario: Append a new node to a non-empty linked list
    Given a linked list with nodes
    When append a new node
    Then new_node should be appended to non-empty linked list