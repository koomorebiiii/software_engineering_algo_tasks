import pytest

from tasks.data_structures.double_connected_node.solution import solution, DoubleConnectedNode

def test_reverse_four_nodes():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)
    assert new_head is node3
    assert new_head.value == "node3"
    assert node3.next is node2
    assert node2.prev is node3
    assert node2.next is node1
    assert node1.prev is node2
    assert node1.next is node0
    assert node0.prev is node1
    assert node0.next is None

def test_reverse_single_node():
    node = DoubleConnectedNode("single")
    new_head = solution(node)
    assert new_head is node
    assert new_head.next is None
    assert new_head.prev is None

def test_reverse_two_nodes():
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0

    new_head = solution(node0)
    assert new_head is node1
    assert node1.next is node0
    assert node0.prev is node1
    assert node0.next is None
    assert node1.prev is None

def test_reverse_three_nodes():
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1

    new_head = solution(node0)
    assert new_head is node2
    assert node2.next is node1
    assert node1.prev is node2
    assert node1.next is node0
    assert node0.prev is node1
    assert node0.next is None
    assert node2.prev is None

def test_reverse_five_nodes():
    node4 = DoubleConnectedNode("node4")
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    new_head = solution(node0)
    assert new_head is node4
    assert node4.next is node3
    assert node3.prev is node4
    assert node3.next is node2
    assert node2.prev is node3
    assert node2.next is node1
    assert node1.prev is node2
    assert node1.next is node0
    assert node0.prev is node1
    assert node0.next is None
    assert node4.prev is None

def test_reverse_none():
    assert solution(None) is None