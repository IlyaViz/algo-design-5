from .crossover_strategy_base import CrossoverStrategyBase


class CycleCrossoverStrategy(CrossoverStrategyBase):
    def crossover(parent1: list, parent2: list) -> list:
        length = len(parent1)

        child = [None] * length

        index = 0

        while None in child:
            if child[index] is not None:
                break

            child[index] = parent1[index]
            
            index = parent2.index(parent1[index])

        for gen_number in range(length):
            if child[gen_number] is None:
                child[gen_number] = parent2[gen_number]

        return child