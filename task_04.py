class BinarySearchTree:
    def __init__(self, preorder_list):

        self._preorder_list_without_zeros = [x for x in preorder_list if x != 0]

        self._root = None
        self._create_tree_from_array_pre_order(preorder_list)
        self._from_tree_to_bst()

    def _from_tree_to_bst(self):
        from copy import deepcopy as dc

        check_tree = dc(self)
        sorted_list = sorted(self._preorder_list_without_zeros)
        node = self._root
        check_node = check_tree._root

        while sorted_list:

            while node.left.value != 0:
                if check_node.left.value == 0:
                    break
                node = node.left
                check_node = check_node.left

            if check_node.value:  # != 0
                node.value = sorted_list.pop(0)
                check_node.value = 0

            if node.right.value != 0 and check_node.right.value != 0:
                node = node.right
                check_node = check_node.right
                continue

            node = node.parent
            check_node = check_node.parent

    def _create_tree_from_array_pre_order(self, arr, node=None):
        if not arr:
            return

        if self._root is None:
            self._root = Node(arr.pop(0))
            self._create_tree_from_array_pre_order(arr, node=self._root)

        elif node.value == 0 or (node.left is not None and node.right is not None):
            self._create_tree_from_array_pre_order(arr, node=node.parent)

        elif node.left is None:
            node.left = Node(arr.pop(0), parent=node)
            self._create_tree_from_array_pre_order(arr, node=node.left)

        elif node.left.value == 0:
            node.right = Node(arr.pop(0), parent=node)
            self._create_tree_from_array_pre_order(arr, node=node.right)

        elif node.right is None:
            node.right = Node(arr.pop(0), parent=node)
            self._create_tree_from_array_pre_order(arr, node=node.right)

    def root(self):
        return self._root

    def parent(self, x):
        return x.parent

    def left(self, x):
        return x.left

    def right(self, x):
        return x.right

    def key(self, x):
        return x.value

    def find_sum(self, s):
        pass


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


bst = BinarySearchTree([1, 4, 6, 10, 0, 0, 0, 7, 0, 8, 0, 0, 2, 5, 0, 0, 3, 9, 0, 0, 0])
print(bst._root.right.value)
print(bst._root.value)