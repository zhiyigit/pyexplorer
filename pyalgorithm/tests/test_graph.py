from algorithms.hello import greetings
from algorithms.graph.graph import Graph
from algorithms.graph.node import Node


def test_graph_has_cycle_false():
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


def test_graph_has_cycle_2nodes_true():
    graph = Graph()

    node101 = Node(101)
    node102 = Node(102)

    graph.add_edge(node102, node101)
    graph.add_edge(node101, node102)

    assert graph.has_cycle() is True



def test_graph_has_cycle_true():
    graph = Graph()

    node101 = Node(101)
    node102 = Node(102)
    node201 = Node(201)
    node202 = Node(202)
    node301 = Node(301)
    node302 = Node(302)
    node401 = Node(401)
    node402 = Node(402)

    graph.add_edge(node201, node101)
    graph.add_edge(node201, node102)
    graph.add_edge(node202, node101)
    graph.add_edge(node301, node201)
    graph.add_edge(node301, node202)
    graph.add_edge(node301, node202)
    graph.add_edge(node302, node202)
    graph.add_edge(node402, node202)
    graph.add_edge(node401, node301)
    graph.add_edge(node401, node302)
    graph.add_edge(node202, node401)

    graph.print()

    assert graph.has_cycle() is True
