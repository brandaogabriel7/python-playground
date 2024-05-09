class Node:
    next_node = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            
            current = current.next_node

        return None
    
    def prepend(self, key, value):
        new_node = Node(key, value)
        if self.head is not None:
            new_node.next_node = self.head

        self.head = new_node

    def remove(self, key):
        if self.head and self.head.key == key:
            self.head = self.head.next_node
        
        previous = self.head

        while previous and previous.next_node:
            current = previous.next_node
            if current.key == key:
                previous.next_node = current.next_node
            
            previous = current

class MyHashMap(object):
    MAX_SIZE = 1000

    def __init__(self):
        self.map = [LinkedList() for _ in range(self.MAX_SIZE)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._get_index(key)
        linked_list = self.map[index]

        entry = linked_list.get(key)
        if not entry:
            linked_list.prepend(key, value)
            return
        
        entry.value = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self._get_index(key)
        linked_list = self.map[index]

        entry = linked_list.get(key)
        if not entry:
            return -1        
        return entry.value

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._get_index(key)
        linked_list = self.map[index]

        linked_list.remove(key)

    def _get_index(self, key):
        return key % self.MAX_SIZE