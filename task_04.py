import sys

sys.setrecursionlimit(4500)


class BinarySearchTree:
    def __init__(self, preorder_list):

        self._preorder_list_without_zeros = [x for x in preorder_list if x != 0]

        self._root = None
        self._create_tree_from_array_pre_order(preorder_list)
        self._from_tree_to_bst()

    def __str__(self):
        li = [self.root()]
        st = ""
        while li:
            for x in li:
                st += str(x.value) + " "
            new_li = list()
            for x in li:
                if x.left is not None:
                    new_li.append(x.left)

                if x.right is not None:
                    new_li.append(x.right)
            li = new_li
            st += "\n"
        return st

    def _from_tree_to_bst(self):

        check_tree = self
        sorted_list = sorted(self._preorder_list_without_zeros)
        node = self._root
        check_node = check_tree._root

        while sorted_list:

            while node.left.value != 0:
                if check_node.left.mark == 0:
                    break
                node = node.left
                check_node = check_node.left

            if check_node.mark:  # != 0
                node.value = sorted_list.pop(0)
                check_node.mark = 0

            if node.right.value != 0 and check_node.right.mark != 0:
                node = node.right
                check_node = check_node.right
                continue

            node = node.parent
            check_node = check_node.parent

    def _dc(self, li):
        """
        alternative for deepcopy
        :param li: list
        :return: list
        """
        if li is None:
            return None
        new_li = list()
        for i in li:
            new_li.append(i)
        return new_li

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
        if x.left is None:
            return x.left
        if x.left.value != 0:
            return x.left
        return None

    def right(self, x):
        if x.right is None:
            return x.right
        if x.right.value != 0:
            return x.right
        return None

    def key(self, x):
        if x is None:
            return x.va
        if x.value != 0:
            return x.value
        return None

    def find_sum(self, s):

        li = []

        # lili = []

        def go_through_branch(root, a, path=None):

            path = self._dc(path)

            if root is None:
                return

            if root.value == 0:
                return

            if path is None:
                path = []

            path.append(root)

            a -= root.value

            if root.left is not None:
                go_through_branch(root.left, s)
            if root.right is not None:
                go_through_branch(root.right, s)

            if a == 0:
                # lili.append([x.value for x in path])
                li.append(path)
                return

            elif a < 0:
                return

            if root.right is not None:
                go_through_branch(root.right, a, path=path)

            if root.left is not None:
                go_through_branch(root.left, a, path=path)

        def rebuild_references(ref_li):
            new_list = list()
            new_list.append(ref_li[-1])

            for _ in range(len(ref_li) - 1):
                new_list.append(new_list[-1].parent)

            return new_list

        go_through_branch(self.root(), s)

        new_li = []
        for k in li:
            k = rebuild_references(k)
            k.reverse()
            if k not in new_li:
                new_li.append(k)

        return new_li


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.mark = value
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


bst = BinarySearchTree([1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0])
print(bst)
arr = bst.find_sum(4)

for i in arr:
    for j in i:
        print(j, j.parent)
    print("---")
