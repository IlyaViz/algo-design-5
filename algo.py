import networkx as nx
import random
from crossover_strategies.crossover_strategy_base import CrossoverStrategyBase
from mutate_strategies.mutate_strategy_base import MutateStrategyBase
from local_improvement_strategies.local_improvement_strategy_base import LocalImprovementStrategyBase
from constants import CITY_NAME_TEMPLATE


class TSP_GA:
    GENERATIONS = 150
    MUTATE_RATE = 0.05
    TOURNAMENT_RATE = 0.15

    def __init__(self, graph: nx.Graph, crossover_strategy: CrossoverStrategyBase, mutate_strategy: MutateStrategyBase, local_improvement_strategy: LocalImprovementStrategyBase, log_every: int) -> list:
        self.graph = graph
        self.crossover_strategy = crossover_strategy
        self.mutate_strategy = mutate_strategy
        self.local_improvement_strategy = local_improvement_strategy
        self.population_size = graph.number_of_nodes() // 2
        self.log_every = log_every
        self.solve_log = []

    def solve(self) -> list:
        init_population = self.get_init_population()

        for iter in range(self.GENERATIONS):
            if iter % self.log_every == 0:
                self.solve_log.append((iter, self.evaluate_individual(self.get_best_individual(init_population))))

            parent1, parent2 = self.tournament_select_parents(init_population, int(self.population_size * self.TOURNAMENT_RATE))

            child = self.crossover_strategy.crossover(parent1, parent2)

            if random.random() <= self.MUTATE_RATE:
                self.mutate_strategy.mutate(child)

            self.local_improvement_strategy.improve(child, self.evaluate_individual)

            init_population.append(child)
            self.remove_worst_individual(init_population)

        best_individual = self.get_best_individual(init_population)
        best_distance = self.evaluate_individual(best_individual)

        best_individual.append(best_individual[0])

        best_distances = [self.graph[f"{CITY_NAME_TEMPLATE}{best_individual[index]}"][f"{CITY_NAME_TEMPLATE}{best_individual[index+1]}"]["length"] for index in range(len(best_individual)-1)]
        best_distances.insert(0, 0)

        return best_distance, best_individual, best_distances

    def get_init_population(self) -> list:
        return [random.sample(range(self.graph.number_of_nodes()), self.graph.number_of_nodes()) for _ in range(self.population_size)]
    
    def get_best_individual(self, population: list) -> int:
        best_individual = population[0]
        
        for individual in population:
            if self.evaluate_individual(individual) < self.evaluate_individual(best_individual):
                best_individual = individual

        return best_individual

    def remove_worst_individual(self, population: list) -> None:
        worst_individual = population[0]

        for individual in population:
            if self.evaluate_individual(individual) > self.evaluate_individual(worst_individual):
                worst_individual = individual

        population.remove(worst_individual)

    def tournament_select_parents(self, population: list, tournament_size: int) -> list:
        parent1 = self.tournament(population, tournament_size)
        parent2 = self.tournament(population, tournament_size)

        return parent1, parent2
    
    def tournament(self, population: list, tournament_size: int) -> list:
        tournament = random.sample(population, tournament_size)

        best_individual = min(tournament, key=self.evaluate_individual)

        return best_individual
    
    def evaluate_individual(self, individual: list) -> int:
        length = 0

        for index in range(len(individual)-1):
            city_number = individual[index]
            neighbour_number = individual[index+1]
            length += self.graph[f"{CITY_NAME_TEMPLATE}{city_number}"][f"{CITY_NAME_TEMPLATE}{neighbour_number}"]["length"] 

        length += self.graph[f"{CITY_NAME_TEMPLATE}{individual[-1]}"][f"{CITY_NAME_TEMPLATE}{individual[0]}"]["length"] 

        return length
