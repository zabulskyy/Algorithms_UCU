import random

ARRAY_SIZE = 1000


class HashTable:
    def __str__(self):
        s = ""
        for i in self.table:
            s += str(i) + "\n"
        return s

    def __init__(self, hash_type, values):
        self.hash_type = hash_type
        self.values = values
        self.table = list(None for _ in range(ARRAY_SIZE))
        self.collisions = 0
        self.fill_table()

    def fill_table(self):
        if self.hash_type == 1 or self.hash_type == 2:
            for number in self.values:
                index = hash_function(number, self.hash_type)
                node = self.table[index]
                if node is None:
                    self.table[index] = Node(number)
                else:
                    self.collisions += 1
                    while node.next_node is not None:
                        node = node.next_node
                    node.next_node = Node(number)

    def get_collisions_amount(self):
        return self.collisions

    def find_sum(self, s):
        if self.hash_type == 1 or self.hash_type == 2:
            for number in self.values:
                number_to_search = s - number
                number_in_table = self.table[hash_function(number_to_search, self.hash_type)]
                if number_in_table is None:
                    continue
                else:
                    return number_in_table.value, number
            return None


def hash_function(n, hash_type, key_list=list()):
    m = 6067
    if hash_type == 1:
        return int((n % m) % ARRAY_SIZE)
    elif hash_type == 2:
        return int(m * n * 1.61803398875 % ARRAY_SIZE)
    return 0


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        if self.next_node is None:
            return str(self.value)
        return str(self.value) + "\t-->\t " + str(self.next_node)


li = list(random.randrange(1000) for _ in range(1000))
t1 = HashTable(1, li)
t2 = HashTable(2, li)

print(t1)
print(t2)

print(t1.get_collisions_amount())
print(t2.get_collisions_amount())
