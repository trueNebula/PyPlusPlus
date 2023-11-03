class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, cap = 100) -> None:
        self.capacity = cap
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def hash(self, key) -> int:
        key = str(key)
        hashsum = 0

        for char in key:
            hashsum += ord(char)

        return hashsum % self.capacity
    
    def insert(self, value) -> None:
        exists = self.find(value)
        if exists is not None:
            return exists

        self.size += 1
        index = self.hash(value)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(self.size, value)
            return self.size
        
        prev = node 
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(self.size, value)
        return self.size

    def find(self, value):
        index = self.hash(value)
        node = self.buckets[index]

        while node is not None and node.value != value:
            node = node.next

        if node is None:
            return None
        
        return node.key

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        
        self.size -= 1
        result = node.value

        if prev is None:
            node = None

        else:
            prev.next = prev.next.next

        return result
    
    def size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        string = ""

        for i in self.buckets:
            if i is None:
                continue

            string += f"{i.key} -> "
            
            while i is not None:
                string += f"{i.value} | "
                i = i.next

            string += "\n"

        if string == "":
            return "{}"
        
        return string[:-1]
        