class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

    


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        coded = key.encode()
        for i in coded:
            hash = (( hash << 5) + hash) + i
        
        return hash
        

        
        
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """


        #creating a new node with key/value pair
        new_entry = HashTableEntry(key, value)
        
        index = self.hash_index(key)
        
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = new_entry
                return
            current_node = self.storage[index]

            while current_node.next is not None:
                if current_node.key == key:
                    current_node = new_entry
                current_node = current_node.next
            current_node.next = new_entry

        else:
            self.storage[index] = new_entry






    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None
            else:
                current = self.storage[index]
                while current.next is not None:
                    if current.key == key:
                       current = None
                    current = current.next

                  
        else: 
            print(f"Error: {key} not found ")





    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        
        if self.storage[index]:
            if self.storage[index].key == key:
                return self.storage[index].value
            
            else:
                current_index = self.storage[index]
                while current_index is not None:
                    if current_index.key == key:
                        return current_index.value
                    current_index = current_index.next
        else:
            return None



    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing.
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
