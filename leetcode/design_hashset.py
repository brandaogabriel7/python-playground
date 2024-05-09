class Node:
    next_node = None

    def __init__(self, value):
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next_node = self.head

        self.head = new_node

    def contains(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            
            current = current.next_node

        return False

    def remove(self, target):
        if self.head and self.head.value == target:
            self.head = self.head.next_node
        
        previous = self.head

        while previous and previous.next_node:
            current = previous.next_node
            if current.value == target:
                previous.next_node = current.next_node
            
            previous = current

class MyHashSet(object):

    MAX_SIZE = 10000

    def __init__(self):
        self.values = [LinkedList() for _ in range(self.MAX_SIZE)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._get_index(key)
        
        linked_list = self.values[index]

        if not linked_list.contains(key):
            linked_list.prepend(key)
            
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._get_index(key)
        
        linked_list = self.values[index]

        linked_list.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self._get_index(key)

        linked_list = self.values[index]

        return linked_list.contains(key)
        
    def _get_index(self, value):
        return value % self.MAX_SIZE