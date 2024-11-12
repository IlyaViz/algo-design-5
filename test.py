import time 
from matplotlib import pyplot as plt
from generator import generate_country_graph
from algo import TSP_GA
from constants import CITY_COUNT, MIN_DISTANCE, MAX_DISTANCE
from crossover_strategies.crossover_strategy_ordered import OrderedCrossoverStrategy
from crossover_strategies.crossover_strategy_PMX import PMXCrossoverStrategy
from crossover_strategies.crossover_strategy_cycle import CycleCrossoverStrategy
from local_improvement_strategies.local_improvement_strategy_swap import SwapImprovementStrategy
from local_improvement_strategies.local_improvement_strategy_insert import InsertImprovementStrategy
from mutate_strategies.mutate_strategy_swap import SwapMutateStrategy
from mutate_strategies.mutate_strategy_reverse import ReverseMutateStrategy


def test_correctness(individual):
    for city_number in range(len(individual)):
        if individual.count(city_number) != 1:
            return False
        
    return True

if __name__ == "__main__":
    graph = generate_country_graph(CITY_COUNT, MIN_DISTANCE, MAX_DISTANCE)

    start = time.time()

    for crossover_strategy in (OrderedCrossoverStrategy, PMXCrossoverStrategy, CycleCrossoverStrategy):
        for local_impovement_strategy in (SwapImprovementStrategy, InsertImprovementStrategy):
            for mutate_strategy in (SwapMutateStrategy, ReverseMutateStrategy):
                algo = TSP_GA(graph, crossover_strategy, mutate_strategy, local_impovement_strategy, 1)
                result = algo.solve()

                x = [point[0] for point in algo.solve_log]
                y = [point[1] for point in algo.solve_log]
                
                plt.figure()
                plt.plot(x, y)
                plt.title(f"{crossover_strategy.__name__},{local_impovement_strategy.__name__},{mutate_strategy.__name__}")
                plt.xlabel('Iterations')
                plt.ylabel('Target function (distance)')

                print(test_correctness(result[1]))
    
    plt.show()

    end = time.time()
    print(end-start)

