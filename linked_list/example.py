# https://realpython.com/linked-lists-python/
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.length = 0
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.length += 1
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                self.length += 1

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.length

    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def add_last(self, node):
        self.length += 1
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                return

        raise Exception("Node with data %s not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                self.length += 1
                return
            prev_node = node

        raise Exception("Node with data %s not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head

        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node

        raise Exception("Node with data %s not found" % target_node_data)

    def __getitem__(self, key):
        if key >= self.length:
            raise IndexError("linked list out of range")

        node = self.head
        while key:
            key -= 1
            node = node.next

        return node.data

    def reverse(self):
        reversed = LinkedList()
        for node in self:
            reversed.add_first(Node(node.data))
        return reversed
