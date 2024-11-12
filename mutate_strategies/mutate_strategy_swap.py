import random
from .mutate_strategy_base import MutateStrategyBase


class SwapMutateStrategy(MutateStrategyBase):
    def mutate(individual):
        length = len(individual)
        
        gen_number1, gen_number2 = random.sample(range(length), 2)

        individual[gen_number1], individual[gen_number2] = individual[gen_number2], individual[gen_number1]