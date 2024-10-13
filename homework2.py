from dataclasses import dataclass


@dataclass
class Node:
    index: int
    aii: list[int]  # для удобства
    fii: list[int]

    @property
    def weight(self) -> int:
        result = 0
        for step in range(len(self.aii)):
            result += self.aii[step] * self.fii[step]
        return result

    def future_weight(self, f_index: int, value: int) -> int:
        result = 0
        for step in range(len(self.aii)):
            if step == f_index:
                result += self.aii[step] * value
            else:
                result += self.aii[step] * self.fii[step]

        return result


class Storage:
    def __init__(self, a_params: list[int], f_itie: list[list[int]]) -> None:
        self.nodes = [Node(index, a_params, fi) for index, fi in enumerate(f_itie)]
        self.storage = {index: node for index, node in enumerate(self.nodes)}
        self.nodes.sort(key=lambda node: node.weight, reverse=True)

    def get_k_popular(self, k: int) -> str:
        return ' '.join(str(self.nodes[step].index + 1) for step in range(k))

    def set_new_coef(self, node_num: int, fi_index: int, value: int) -> None:
        node = self.storage[node_num - 1]
        current_node_index = self.__find_node_index(node)
        weight = node.future_weight(fi_index, value)
        new_index = binary_search(self.nodes, weight)
        node.fii[fi_index] = value

        if current_node_index > new_index:
            self.nodes = (
                self.nodes[:new_index] +
                [node] +
                self.nodes[new_index:current_node_index] +
                self.nodes[current_node_index + 1:]
            )
        else:
            self.nodes = (
                self.nodes[:current_node_index] +
                self.nodes[current_node_index + 1:new_index] +
                [node] +
                self.nodes[new_index:]
            )

    def __find_node_index(self, node_to_find: Node) -> int:
        for index, node in enumerate(self.nodes):
            if node_to_find is node:
                return index

        raise ValueError(f'Unexpected case. We had to find the node')


def binary_search(array: list[Node], elem: int) -> int:
    return _binary_search(array, elem, 0, len(array) - 1)


def _binary_search(array: list[Node], elem: int, left: int, right: int) -> int:
    if right <= left:
        return left + 1 if elem < array[right].weight else left

    mid = (right + left) // 2
    if array[mid].weight == elem:
        return mid

    if elem < array[mid].weight:
        return _binary_search(array, elem, mid + 1, right)

    return _binary_search(array, elem, left, mid - 1)


if __name__ == '__main__':
    n = int(input())
    a_params = [int(a) for a in input().split()]
    d_rank_cnt = int(input())
    f_itie = [[int(fj) for fj in input().split()] for _ in range(d_rank_cnt)]
    q_requests_cnt = int(input())
    requests = [[int(item) for item in input().split()] for _ in range(q_requests_cnt)]
    storage = Storage(a_params, f_itie)
    for req_type, *args in requests:
        if req_type == 1:
            print('result:', storage.get_k_popular(*args))
        elif req_type == 2:
            storage.set_new_coef(*args)


"""  
2
1 100
10
1 2
2 1
3 1
4 1
5 1
6 1
7 1
8 1
9 1
10 1
6
1 2
1 10
2 4 1 1000
1 10
2 4 1 1
1 10
"""
