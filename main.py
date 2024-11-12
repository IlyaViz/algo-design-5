from algo import TSP_GA
from generator import generate_country_graph
from constants import CITY_COUNT, MIN_DISTANCE, MAX_DISTANCE
from crossover_strategies.crossover_strategy_ordered import OrderedCrossoverStrategy
from crossover_strategies.crossover_strategy_PMX import PMXCrossoverStrategy
from crossover_strategies.crossover_strategy_cycle import CycleCrossoverStrategy
from local_improvement_strategies.local_improvement_strategy_swap import SwapImprovementStrategy
from local_improvement_strategies.local_improvement_strategy_insert import InsertImprovementStrategy
from mutate_strategies.mutate_strategy_swap import SwapMutateStrategy
from mutate_strategies.mutate_strategy_reverse import ReverseMutateStrategy


if __name__ == "__main__":
    crossover_strategies = [OrderedCrossoverStrategy, PMXCrossoverStrategy, CycleCrossoverStrategy]
    local_impovement_strategies = [SwapImprovementStrategy, InsertImprovementStrategy]
    mutate_strategies = [SwapMutateStrategy, ReverseMutateStrategy]

    crossover_strategy = crossover_strategies[int(input("OrderedCrossoverStrategy [0], PMXCrossoverStrategy [1], CycleCrossoverStrategy [2]\n"))]
    local_impovement_strategy = local_impovement_strategies[int(input("SwapImprovementStrategy [0], InsertImprovementStrategy [1]\n"))]
    mutate_strategy = mutate_strategies[int(input("SwapMutateStrategy [0], ReverseMutateStrategy [1]\n"))]

    graph = generate_country_graph(CITY_COUNT, MIN_DISTANCE, MAX_DISTANCE)

    algo = TSP_GA(graph, crossover_strategy, mutate_strategy, local_impovement_strategy, 25)

    result = algo.solve()

    for city, distance in zip(result[1], result[2]):
        print(f"Go to city: {city}, distance: {distance}")

    print(result[0])
