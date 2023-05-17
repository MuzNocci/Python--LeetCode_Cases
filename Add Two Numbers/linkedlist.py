from list_node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        return self._size
    
    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')       
        if pointer:
            return pointer.data
        raise IndexError('list index out of range')
    
    def setitem(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list index out fo range')
    


lista = LinkedList()

lista.append(5)
lista.append(7)
lista.append(11)
lista.append(2)
print(lista[1])
print(lista._size)
