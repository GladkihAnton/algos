class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        return f'Node({self.data})'

    def __repr__(self):
        return f'Node({self.data})'


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def inverse_tree(self):
        pass

    def beautiful_print(self):
        if self.root is None:
            print('The tree is empty')
            return

        height = self.height()
        result: list[Node | None] = [None] * (2 ** height)
        result[0] = self.root
        self.__fill_array(result, self.root.left, 1)
        self.__fill_array(result, self.root.right, 2)
        to_print = []
        for depth in range(height):
            to_print.append([result[2**depth + node_index - 1] for node_index in range(2 ** depth)])

        to_print_final = []
        max_columns = sum(2**i for i in range(height))
        for depth, node_on_depth in enumerate(to_print):
            string_elements_per_depth = [None] * max_columns

            start_step = max_columns // 2 ** (depth + 1)
            step_between = max_columns // 2 ** depth
            for index, node in enumerate(node_on_depth):
                string_elements_per_depth[
                    start_step + index * (step_between + 1)
                ] = node.data if node is not None else 'XX'
            to_print_final.append(
                ' '.join(
                    '  ' if elem is None else str(elem).zfill(2) for elem in string_elements_per_depth
                )
            )
        print('\n'.join(to_print_final))

    def __revert_node(self, node: Node) -> None:
        node.right, node.left = node.left, node.right

        if node.right is not None:
            self.__revert_node(node.right)

        if node.left is not None:
            self.__revert_node(node.left)

    def revert_tree(self) -> None:
        if self.root is None:
            return

        self.__revert_node(self.root)

    def __fill_array(self, arr: list[Node | None], node: Node, index: int) -> None:
        if arr[index] is not None:
            raise ValueError(f'Must be None {index=}, {node}')

        arr[index] = node

        if node.left is not None:
            self.__fill_array(arr, node.left, 2 * index + 1)

        if node.right is not None:
            self.__fill_array(arr, node.right, 2 * index + 2)

    def tree_print(self):
        self.__tree_print(self.root)

    def tree_walk_horisontal(self):
        if self.root is not None:
            self.__tree_walk_hor([self.root])

    def __tree_walk_hor(self, nodes: list):
        new_list = []
        if len(nodes) == 0:
            return
        for obj in nodes:
            print(obj.data, end=" ")
            if obj.left is not None:
                new_list.append(obj.left)
            if obj.right is not None:
                new_list.append(obj.right)
        print()
        self.__tree_walk_hor(new_list)

    def __tree_print(self, node):
        if node is not None:
            print(node.data)
            print("left", node.left.data if (node.left is not None) else None)
            print("right", node.right.data if (node.right is not None) else None)
            print('-' * 100)
            self.__tree_print(node.left)
            self.__tree_print(node.right)

    def __height(self, node):
        if node is None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def height(self):
        if self.root is None:
            return 0
        return self.__height(self.root)

    def bfs(self):
        for i in range(self.height()):
            self.level_print(self.root, i)
            print()

    def level_print(self, node, level):
        if node is None:
            return
        if level == 0:
            print(node.data, end=' ')
        self.level_print(node.left, level - 1)
        self.level_print(node.right, level - 1)

    def __delete(self, node, elem):
        if node is not None:
            if node.left is not None:
                if elem == node.left.data:
                    right = node.left.right
                    node = node.left.left
                    node
            if node.right is not None:
                if elem == node.right.data:
                    nodeSave = None
                    if node.right.left is not None:
                        if node.right.left.right is not None:
                            nodeSave = node.right.left.right
                        oldRight = node.right.right
                        node.right = node.right.left
                        node.right.right = oldRight

            self.__delete(node.left, elem)
            self.__delete(node.right, elem)

    def delete(self, elem):
        if self.root is None:
            return
        self.__delete(self.root, elem)

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while node is not None:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                elif data > node.data:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right
                else:
                    break


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.tree_print()
    tree.add(20)
    tree.add(60)
    tree.add(8)
    tree.add(7)
    tree.add(27)
    tree.add(96)
    tree.add(23)
    tree.add(53)

    tree.tree_print()
    tree.beautiful_print()
    tree.revert_tree()
    tree.beautiful_print()
