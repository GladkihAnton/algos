from typing import Optional


class Node:
    def __init__(self, d):
        self.data = d
        self.next: Optional['Node'] = None

    def __str__(self):
        return f'Node({self.data})'

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size = 0

    def get_last(self):
        iter = self.head
        if iter is not None:
            while iter.next is not None:
                iter = iter.next
            return iter
        return None

    def __get_last_rec(self, node):
        if node.next is None:
            return node
        else:
            return self.__get_last_rec(node.next)

    def get_last_rec(self):
        if self.head is None:
            return None
        return self.__get_last_rec(self.head)

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.get_last_rec()
            last.next = new_node
        self.size += 1

    def __print_list(self, node):
        print(node.data, end='')
        if node.next is not None:
            print(' -> ', end='')
            self.__print_list(node.next)

    def print_list(self):
        if self.head is not None:
            self.__print_list(self.head)

    def insert(self, data, n):
        if n < self.size:
            iter = self.head
            prev = None
            for i in range(n):
                prev = iter
                iter = iter.next
            new_node = Node(data)
            if prev is not None:
                prev.next = new_node
            new_node.next = iter

    def __reverse_rec(self, node: Node, linked_list: 'LinkedList') -> None:
        if node.next is not None:
            self.__reverse_rec(node.next, linked_list)

        linked_list.add(node.data)

    def reverse_rec(self) -> 'LinkedList':
        """
        Reverse recursive and return new linked list
        """

        new_linked_list = LinkedList()

        if self.head is None:
            return new_linked_list

        self.__reverse_rec(self.head, new_linked_list)
        return new_linked_list

    def reverse_iter_inplace(self) -> None:
        """
        Reverse inplace using iterator and return new linked list
        """
        if self.head is None:
            return

        node = self.head
        next_node = self.head.next
        node.next = None
        while next_node is not None:
            next_next_node = next_node.next
            next_node.next = node
            node = next_node
            next_node = next_next_node

        self.head = node


if __name__ == '__main__':
    # Через рекурсию в обратную сторону заполняем новый линдек лист.
    # Так же отдельным методов "на месте" меняем итеративно
    # Поменял формат вывод на более красивый
    ll = LinkedList()
    ll.add(5)
    ll.add(3)
    ll.add(2)
    ll.add(6)
    ll.print_list()
    ll.reverse_iter_inplace()
    print()
    ll.print_list()

    print()
    new_ll = ll.reverse_rec()
    new_ll.print_list()
