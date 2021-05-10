from LinkedList import LinkedList

class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of
    # its elements with a LinkedList object.
    def create_arr(self, size):
        return [LinkedList() for _ in range(size)]

    # Hash functions are a function that turns each of these keys into an index
    # value that we can use to decide where in our list each key:value pair
    # should be stored.
    def hash_func(self, key):
        """A hash function that mods the sum of ASCII codes for each char in key"""
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    # Should insert a key value pair into the hash table, where the key is the
    # word and the value is a counter for the number of times the word appeared.
    # When inserting a new word in the hash table, be sure to check if there is
    # a Node with the same key in the table already.
    def insert(self, key, value):
        h = self.hash_func(key)
        # Searches for item. If it's found, increases frequency by 1
        found = self.arr[h].find([key, value], increase=True)
        if found == -1:  # if the key was not found:
            self.arr[h].append([key, value])

    # Traverse through the every Linked List in the table and print the key value pairs.
    # For example: 
    # a: 1
    # again: 1
    # and: 1
    # blooms: 1
    # erase: 2
    def print_key_values(self):
        for linked_list in self.arr:
            linked_list.print_nodes()
