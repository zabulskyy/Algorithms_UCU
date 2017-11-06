import random


class HashTable:
    def __str__(self):
        s = ""
        for i in self.table:
            s += str(i) + ("\n" if self.hash_type == 1 or self.hash_type == 2 else " ")
        return s

    def __init__(self, hash_type, values):
        self.array_size = len(values) ** 2
        self.hash_type = hash_type
        self.values = values
        self.table = list(None for _ in range(self.array_size))
        self.collisions = 0
        self.fill_table()

    def fill_table(self):
        if self.hash_type == 1 or self.hash_type == 2:
            for number in self.values:
                index = self.hash_function(number)
                node = self.table[index]
                new_node = Node(number)
                if node is None:
                    self.table[index] = new_node
                else:
                    self.collisions += 1
                    new_node.next_node = node
                    self.table[index] = new_node

        if self.hash_type == 3:
            for number in self.values:
                index = self.hash_function(number)
                node = self.table[index]
                while node is not None:
                    index += 1
                    self.collisions += 1
                    node = self.table[index]
                self.table[index] = Node(number)

        if self.hash_type == 4:
            for number in self.values:
                index = self.hash_function(number)
                node = self.table[index]
                add_number = 1
                while node is not None:
                    index += add_number ** 2
                    add_number += 1
                    self.collisions += 1
                    node = self.table[index]
                self.table[index] = Node(number)

    def get_collisions_amount(self):
        return self.collisions

    def find_sum(self, s):
        if self.hash_type == 1 or self.hash_type == 2:
            print(self.values, end=" ")
            for number in self.values:
                number_to_search = s - number
                if number_to_search <= 0:
                    continue
                number_in_table = self.table[self.hash_function(number_to_search)]
                if number_in_table is None:
                    continue
                else:
                    return number_in_table.value, number
            return None
        else:
            for number in self.values:
                pass

    def hash_function(self, n, key_list=list()):
        # m = 6067
        m = 13
        if self.hash_type == 1:
            return int((n % m) % self.array_size)
        else:
            return int(m * n * 1.61803398875 % self.array_size)


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        if self.next_node is None:
            return str(self.value)
        return str(self.value) + "\t-->\t " + str(self.next_node)


li = list(i for i in [42, 4, 99, 8, 54, 13, 4, 12, 89])
t1 = HashTable(1, li)

print(t1.find_sum(100))
print(str(t1))

# t2 = HashTable(2, li)
# t3 = HashTable(3, li)
# t4 = HashTable(4, li)
#
# print(t2)
# print("---")
# print(t3)
# print(t4)
# print(t3.get_collisions_amount())
# print(t4.get_collisions_amount())

# print(t2)
#
# print(t1.get_collisions_amount())
# # print(t2.get_collisions_amount())
#
# print(t1.find_sum(10))
