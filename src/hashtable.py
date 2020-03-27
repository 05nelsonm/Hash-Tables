# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """
        # Hash that key girl
        hashed_key = self._hash_mod(key)

        # Setup temporary variables
        new_lp = LinkedPair(key, value)
        current_lp = self.storage[hashed_key]

        # If it's None, store it.
        if current_lp is None:
            self.storage[hashed_key] = new_lp
            return

        # Check for key match and replace value
        if current_lp.key == key:
            current_lp.value = value
            return

        # Loop through until keys match or next is None
        while current_lp.next:
            current_lp = current_lp.next
            if current_lp.key == key:
                current_lp.value = value
                return

        # If a key was not found in the loop, set next
        current_lp.next = new_lp

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        # Hash that key girl
        hashed_key = self._hash_mod(key)

        # Setup temporary variables
        current_lp = self.storage[hashed_key]

        # Print warning if not found
        if current_lp is None:
            print(f"Key {key} was not found")
            return

        # Loop through until keys match and overwrite with None
        while current_lp:
            if current_lp.key == key:
                current_lp.key = None
                current_lp.value = None
                current_lp = None
                return
            current_lp = current_lp.next

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        # Hash that key girl
        hashed_key = self._hash_mod(key)

        # Setup temporary variables
        current_lp = self.storage[hashed_key]

        # Loop through until key match is found
        while current_lp:
            if current_lp.key == key:
                return current_lp.value

            current_lp = current_lp.next

        # If nothing was found while looping, return None
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        # Copy current storage to temp variable
        old_storage = self.storage

        # Double capacity
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # For every LinkedPair in old storage
        for lp in old_storage:
            current_lp = lp

            # Loop through and insert kvp
            while current_lp:
                self.insert(current_lp.key, current_lp.value)
                current_lp = current_lp.next

        # Celebrate
        return self.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
