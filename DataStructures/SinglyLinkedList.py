class Node:
    __slots__ = ('data', 'next')

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.data

    def __repr__(self):
        return f'Node({self.data})'


class SinglyLinkedList:
    __slots__ = ('head', 'length')

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        output = 'SinglyLinkedList('
        current = self.head
        if not current:
            output += ')'
            return output

        while current.next:
            output += f'{current.data}, '
            current = current.next
        output += f'{current.data}'
        output += ')'
        return output

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if (index > self.length - 1) or (index < 0):
            raise IndexError('DataStructures index out of range')

        i = 0
        current = self.head
        while i < index:
            current = current.next
            i += 1
        return current.data

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def append(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, index, data):
        if (index > self.length - 1) or (index < 0):
            raise IndexError('DataStructures index out of range')
        self.length += 1

        if index == 0:
            current = self.head
            self.head = Node(data)
            self.head.next = current
            return

        i = 0
        prev_node = self.head
        current_node = self.head
        while i < index:
            prev_node = current_node
            current_node = current_node.next
            i += 1

        prev_node.next = Node(data)
        prev_node.next.next = current_node

    def remove(self, index):
        if (index > self.length - 1) or (index < 0):
            raise IndexError('DataStructures index out of range')
        self.length -= 1

        if index == 0:
            current = self.head
            self.head = self.head.next
            del current
            return

        i = 0
        prev_node = self.head
        current_node = self.head
        while i < index:
            prev_node = current_node
            current_node = current_node.next
            i += 1

        prev_node.next = current_node.next
        del current_node
