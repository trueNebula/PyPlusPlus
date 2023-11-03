from hash_table import HashTable

class SymbolTable:
    def __init__(self) -> None:
        self.table = HashTable()

    def insert(self, k, v):
        return self.table.insert(k, v)

    def find(self, k):
        return self.table.find(k)
    
    def remove(self, k):
        return self.table.remove(k)
    
    def size(self) -> int:
        return self.table.size
    
    def __str__(self) -> str:
        return str(self.table)