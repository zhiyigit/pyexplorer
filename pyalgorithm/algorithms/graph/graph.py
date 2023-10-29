from typing import List

from algorithms.graph.node import Node


class Graph:
    graph: dict[Node, List[Node]]

    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node: Node, to_node: Node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def node_has_cycle(
        self, node: Node, df_path: set[Node], verified_nodes: set[Node]
    ) -> bool:
        print(f"checking: {node}")
        """
        print("  df_path: ")
        for one in df_path:
            print(f"             {one}")
        """
        if node in df_path:
            return True

        if node in verified_nodes:
            print(f"  skipping: {node}")
            return False

        if node in self.graph:
            df_path.add(node)

            for next_node in self.graph[node]:
                if self.node_has_cycle(next_node, df_path, verified_nodes):
                    return True

            df_path.remove(node)

        verified_nodes.add(node)
        return False

    def has_cycle(self) -> bool:
        verified_nodes: set[Node] = set()
        for key, value in self.graph.items():
            if key not in verified_nodes:
                df_path: set[Node] = set()
                if self.node_has_cycle(key, df_path, verified_nodes):
                    return True

        return False

    def print(self):
        for key, value in self.graph.items():
            print(f"from: {key}")
            for to_node in value:
                print(f"    to: {to_node}")
