import networkx as nx

def find_shortest_path(graph, source, destination):
    try:
        path = nx.shortest_path(graph, source=source, target=destination)
        return path
    except nx.NetworkXNoPath:
        return None
