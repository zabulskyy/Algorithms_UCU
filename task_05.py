import random


class HashTable:
    def __str__(self):
        s = ""
        for i in self.table:
            s += str(i) + ("\n" if self.hash_type == 1 or self.hash_type == 2 else " ")
        return s

    def __init__(self, hash_type, values):
        self.m = len(values) * 3
        self.hash_type = hash_type
        self.values = values
        self.table = list(None for _ in range(self.m))
        self.collisions = 0
        self.fill_table()

    def fill_table(self):
        if self.hash_type == 1 or self.hash_type == 2:
            for number in self.values:
                index = self.hash_function(number)
                node = Node(number)
                if self.table[index] is None:
                    self.table[index] = node
                else:
                    self.collisions += 1
                    node.next_node = self.table[index]
                    self.table[index] = node

        else:
            for number in self.values:
                index = self.hash_function(number)
                iter = 0
                while  iter < self.m and self.table[index] is not None:
                    index = self.hash_function(number, i=iter)
                    iter += 1
                    self.collisions += 1
                self.table[index] = number

    def find_sum(self, s):
        if self.hash_type == 1 or self.hash_type == 2:
            # counter = 0
            for number in self.values:
                number_to_find = s - number
                index = self.hash_function(number_to_find)
                node_to_check = self.table[index]
                while 1:
                    if node_to_check is None:
                        break
                    if node_to_check.value != number_to_find:
                        node_to_check = node_to_check.next_node
                    else:
                        break

                if node_to_check is not None and node_to_check.value == number_to_find:
                    return node_to_check.value, number

                        # if counter:
                        #     return node_to_check.value, number
                        # else:
                        #     counter = 1
                        #     continue

        else:
            # counter = 0
            for number in self.values:
                number_to_find = s - number
                # if number_to_find <= 0:
                #     continue
                index = self.hash_function(number_to_find)
                number_to_check = self.table[index]
                iter = 0
                while 1:
                    if iter > self.m:
                        break
                    if number_to_check is None:
                        break
                    if number_to_check != number_to_find:
                        number_to_check = self.table[self.hash_function(index, iter)]
                    else:
                        break
                    iter += 1
                if number_to_check is not None and number_to_check == number_to_find:
                    return number_to_check, number
                        # if counter:
                        #     return number_to_check, number
                        # else:
                        #     counter = 1
                        #     continue
        return None

    def get_collisions_amount(self):
        return self.collisions

    def hash_function(self, n, i=0):
        if self.hash_type == 1:
            x = n
        elif self.hash_type == 2:
            x = n * 0.618
        elif self.hash_type == 3:
            x = n + i
        elif self.hash_type == 4:
            x = n + i ** 2
        else:
            x = self.new_hash_function(n) + i * self.new_hash_function(n + 1)
        return int(x) % self.m

    def new_hash_function(self, n):
        return int((n * 0.618) % self.m)


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        if self.next_node is None:
            return str(self.value)
        return str(self.value) + "\t-->\t " + str(self.next_node)


li = list(random.randrange(99999) for i in range(9999))
t1 = HashTable(3, li)

print(t1)
print("---")
print(t1.find_sum(10))



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
