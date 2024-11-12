import networkx as nx
import random
from constants import CITY_NAME_TEMPLATE


def generate_country_graph(city_count: int, min_distance: int, max_distance: int) -> nx.Graph:
    graph = nx.Graph()

    for x in range(city_count):
        graph.add_node(f"{CITY_NAME_TEMPLATE}{x}")

    for x in range(city_count):
        for y in range(city_count):
            if x != y:
                distance = random.randint(min_distance, max_distance)
                graph.add_edge(f"{CITY_NAME_TEMPLATE}{x}", f"{CITY_NAME_TEMPLATE}{y}", length=distance)

    return graph