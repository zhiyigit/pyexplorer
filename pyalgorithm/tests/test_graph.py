from algorithms.graph.graph import Graph
from algorithms.graph.node import Node


def test_graph_has_cycle_true():
    graph = Graph()

    node101 = Node(101)
    node102 = Node(102)
    node201 = Node(201)
    node202 = Node(202)
    node301 = Node(301)

    graph.add_edge(node201, node101)
    graph.add_edge(node201, node102)
    graph.add_edge(node202, node101)
    graph.add_edge(node301, node201)
    graph.add_edge(node301, node202)

    assert graph.has_cycle() is False