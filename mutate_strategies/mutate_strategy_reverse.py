import random
from .mutate_strategy_base import MutateStrategyBase


class ReverseMutateStrategy(MutateStrategyBase):
    def mutate(individual):
        length = len(individual)
        
        gen_number1, gen_number2 = sorted(random.sample(range(length), 2))

        individual[gen_number1:gen_number2+1] = reversed(individual[gen_number1:gen_number2+1])
