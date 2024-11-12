import random
from .crossover_strategy_base import CrossoverStrategyBase


class PMXCrossoverStrategy(CrossoverStrategyBase):
    def crossover(parent1: list, parent2: list) -> list:
        length = len(parent1)

        gen_number1, gen_number2 = sorted(random.sample(range(length), 2))

        child = [None] * length
        child[gen_number1:gen_number2+1] = parent1[gen_number1:gen_number2+1]

        for gen_number in range(length):
            if child[gen_number] is None:
                value = parent2[gen_number]

                while value in child:
                    value = parent1[parent2.index(value)]

                child[gen_number] = value
        
        return child