class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [ [-1] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        shard_id = key%1000
        if self.table[shard_id] == [-1]:
            self.table[shard_id] = [-1]*1000
        chunk_id = key//1000
        self.table[shard_id][chunk_id] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        shard_id = key%1000
        chunk_id = key//1000
        if self.table[shard_id] != [-1] and self.table[shard_id][chunk_id] != -1:
            return self.table[shard_id][chunk_id]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        shard_id = key%1000
        chunk_id = key//1000
        if self.table[shard_id] != [-1] and self.table[shard_id][chunk_id] != -1:
            self.table[shard_id][chunk_id] = -1