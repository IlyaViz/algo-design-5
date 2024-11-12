import random
from .crossover_strategy_base import CrossoverStrategyBase


class OrderedCrossoverStrategy(CrossoverStrategyBase):
    def crossover(parent1: list, parent2: list) -> list:
        length = len(parent1)

        gen_number1, gen_number2 = sorted(random.sample(range(length), 2))

        child = [None] * length
        child[gen_number1:gen_number2+1] = parent1[gen_number1:gen_number2+1]

        pointer = 0

        for gen_number in range(length):
            if parent2[gen_number] not in child:
                while child[pointer] is not None:
                    pointer += 1
                
                child[pointer] = parent2[gen_number]
        
        return child